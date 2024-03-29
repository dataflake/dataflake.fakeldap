##############################################################################
#
# Copyright (c) 2008-2023 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import ldap

from .base import FakeLDAPTests


class MemberOfTests(FakeLDAPTests):

    def _getTargetClass(self):
        from .. import FakeLDAPConnection

        class MemberOfConnection(FakeLDAPConnection):
            """ A FakeLDAPConnection with memberof management enabled
            """
            maintain_memberof = True

        return MemberOfConnection

    def test_connection_is_memberof(self):
        conn = self._makeOne()
        self.assertEqual(conn.maintain_memberof, True)

    def test_add_group_updates_member_attr(self):
        conn = self._makeOne()
        self._addUser('foo')
        self._addUser('bar')
        self._addUser('baz')
        self._addGroup('engineering', ['foo', 'bar'])

        res = conn.search_s('ou=groups,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=engineering)')
        self.assertEqual(sorted(res[0][1][conn.member_attr]),
                         ['cn=bar,ou=users,dc=localhost',
                          'cn=foo,ou=users,dc=localhost'])

    def test_add_group_updates_memberof_attr(self):
        conn = self._makeOne()
        self._addUser('foo')
        self._addUser('bar')
        self._addUser('baz')
        self._addGroup('engineering', ['foo', 'bar'])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=foo)')
        self.assertEqual(res[0][1][conn.memberof_attr],
                         ['cn=engineering,ou=groups,dc=localhost'])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=bar)')
        self.assertEqual(res[0][1][conn.memberof_attr],
                         ['cn=engineering,ou=groups,dc=localhost'])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=baz)')
        self.assertEqual(res[0][1].get(conn.memberof_attr, []), [])

    def test_add_group_member_updates_memberof_attr(self):
        conn = self._makeOne()
        self._addUser('foo')
        self._addUser('bar')
        self._addUser('baz')
        self._addGroup('engineering', ['foo'])

        conn.modify_s('cn=engineering,ou=groups,dc=localhost',
                      [(ldap.MOD_ADD, conn.member_attr,
                       ['cn=bar,ou=users,dc=localhost'])])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=foo)')
        self.assertEqual(res[0][1][conn.memberof_attr],
                         ['cn=engineering,ou=groups,dc=localhost'])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=bar)')
        self.assertEqual(res[0][1][conn.memberof_attr],
                         ['cn=engineering,ou=groups,dc=localhost'])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=baz)')
        self.assertEqual(res[0][1].get(conn.memberof_attr, []), [])

    def test_delete_group_member_updates_memberof_attr(self):
        conn = self._makeOne()
        self._addUser('foo')
        self._addUser('bar')
        self._addUser('baz')
        self._addGroup('engineering', ['foo', 'bar', 'baz'])

        conn.modify_s('cn=engineering,ou=groups,dc=localhost',
                      [(ldap.MOD_DELETE, conn.member_attr,
                       ['cn=foo,ou=users,dc=localhost'])])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=foo)')
        self.assertEqual(res[0][1].get(conn.memberof_attr, []), [])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=bar)')
        self.assertEqual(res[0][1][conn.memberof_attr],
                         ['cn=engineering,ou=groups,dc=localhost'])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=baz)')
        self.assertEqual(res[0][1][conn.memberof_attr],
                         ['cn=engineering,ou=groups,dc=localhost'])

    def test_delete_user_updates_member_attr(self):
        conn = self._makeOne()
        self._addUser('foo')
        self._addUser('bar')
        self._addUser('baz')
        self._addGroup('engineering', ['foo', 'bar', 'baz'])

        conn.delete_s('cn=foo,ou=users,dc=localhost')

        res = conn.search_s('ou=groups,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=engineering)')
        self.assertEqual(sorted(res[0][1][conn.member_attr]),
                         ['cn=bar,ou=users,dc=localhost',
                          'cn=baz,ou=users,dc=localhost'])

    def test_delete_group_updates_memberof_attr(self):
        conn = self._makeOne()
        self._addUser('foo')
        self._addUser('bar')
        self._addUser('baz')
        self._addGroup('engineering', ['foo', 'bar', 'baz'])

        conn.delete_s('cn=engineering,ou=groups,dc=localhost')

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=foo)')
        self.assertEqual(res[0][1].get(conn.memberof_attr, []), [])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=bar)')
        self.assertEqual(res[0][1].get(conn.memberof_attr, []), [])

        res = conn.search_s('ou=users,dc=localhost',
                            ldap.SCOPE_SUBTREE,
                            filterstr='(cn=baz)')
        self.assertEqual(res[0][1].get(conn.memberof_attr, []), [])
