#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Orgs are collections of people who make decisions
after a threshold of consensus. When new admins are
added, the org keys fundimentally change hands.
Operations involving adding or removing citizens,
however, occur under the existing keys.
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime
from ...types import ObjHash, ObjSig, ObjPubKey, ObjAddress, ObjBlob


class OrgConsensusBegin(Command):
    """
    # admin pubkeys, consensus requirements
    """
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]


def OrgConsensusIncrement():
    pass


def OrgConsensusVerify():
    pass
# bio items


def OrgBorderBegin():  # border object [(lat,long),...], yea/nay-date
    pass


def OrgBorderIncrement():
    pass


def OrgBorderVerify():
    pass


def OrgManifestoBegin():  # manifesto (markdown), yea/nay-date
    pass


def OrgManifestoIncrement():
    pass


def OrgManifestoVerify():
    pass
# org couriers:


def OrgStaffCouriersBegin():  # key, ip, voters in favor, admins in favor
    pass


def OrgStaffCouriersIncrement():
    pass


def OrgStaffCouriersVerify():
    pass


def OrgVolunteerCouriersBegin():  # key, ip, voters in favor, admins in favor
    pass


def OrgVolunteerCouriersIncrement():
    pass


def OrgVolunteerCouriersVerify():
    pass
# memberships


def OrgMembershipBegin():  # membership proposal object, yea/nay-date
    pass


def OrgMembershipIncrement():
    pass


def OrgMembershipVerify():
    pass


def OrgProposalBegin():  # proposal object, yea/nay-date
    pass


def OrgProposalIncrement():
    pass


def OrgProposalVerify():
    pass


def OrgVoteTallyBegin():  # vote object, ballots cast, yea/nay-date
    pass


def OrgVoteTallyIncrement():
    pass


def OrgVoteTallyVerify():
    pass


def OrgPollTallyBegin():  # poll object, ballots answered, yea/nay-date
    pass


def OrgPollTallyIncrement():
    pass


def OrgPollTallyVerify():
    pass


def OrgSavesBegin():  # hash to save, yea/nay-date
    pass


def OrgSavesIncrement():
    pass


def OrgSavesVerify():
    pass
