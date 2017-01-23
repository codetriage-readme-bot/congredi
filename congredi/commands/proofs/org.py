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


class OrgConsensusIncrement(Command):
    response = []


class OrgConsensusVerify(Command):
    response = []
# bio items


class OrgBorderBegin(Command):  # border object [(lat,long),...], yea/nay-date
    response = []


class OrgBorderIncrement(Command):
    response = []


class OrgBorderVerify(Command):
    response = []


class OrgManifestoBegin(Command):  # manifesto (markdown), yea/nay-date
    response = []


class OrgManifestoIncrement(Command):
    response = []


class OrgManifestoVerify(Command):
    response = []
# org couriers:


# key, ip, voters in favor, admins in favor
class OrgStaffCouriersBegin(Command):
    response = []


class OrgStaffCouriersIncrement(Command):
    response = []


class OrgStaffCouriersVerify(Command):
    response = []


# key, ip, voters in favor, admins in favor
class OrgVolunteerCouriersBegin(Command):
    response = []


class OrgVolunteerCouriersIncrement(Command):
    response = []


class OrgVolunteerCouriersVerify(Command):
    response = []
# memberships


class OrgMembershipBegin(Command):  # membership proposal object, yea/nay-date
    response = []


class OrgMembershipIncrement(Command):
    response = []


class OrgMembershipVerify(Command):
    response = []


class OrgProposalBegin(Command):  # proposal object, yea/nay-date
    response = []


class OrgProposalIncrement(Command):
    response = []


class OrgProposalVerify(Command):
    response = []


class OrgVoteTallyBegin(Command):  # vote object, ballots cast, yea/nay-date
    response = []


class OrgVoteTallyIncrement(Command):
    response = []


class OrgVoteTallyVerify(Command):
    response = []


class OrgPollTallyBegin(Command):  # poll object, ballots answered, yea/nay-date
    response = []


class OrgPollTallyIncrement(Command):
    response = []


class OrgPollTallyVerify(Command):
    response = []


class OrgSavesBegin(Command):  # hash to save, yea/nay-date
    response = []


class OrgSavesIncrement(Command):
    response = []


class OrgSavesVerify(Command):
    response = []


class orgResponders(object):
    redis = None
    neo4j = None

    def __init__(self):
        # would pulll Redis online
        pass

    @OrgConsensusBegin.responder
    def ConsensusBegin(self):
        pass

    @OrgConsensusIncrement.responder
    def ConsensusIncrement(self):
        pass

    @OrgConsensusVerify.responder
    def ConsensusVerify(self):
        pass
    # bio items

    @OrgBorderBegin.responder  # border object [.responder
    def BorderBegin(self):  # border object [(lat,long),...], yea/nay-date
        pass

    @OrgBorderIncrement.responder
    def BorderIncrement(self):
        pass

    @OrgBorderVerify.responder
    def BorderVerify(self):
        pass

    @OrgManifestoBegin.responder  # manifesto .responder
    def ManifestoBegin(self):  # manifesto (markdown), yea/nay-date
        pass

    @OrgManifestoIncrement.responder
    def ManifestoIncrement(self):
        pass

    @OrgManifestoVerify.responder
    def ManifestoVerify(self):
        pass
    # org couriers:

    @OrgStaffCouriersBegin.responder
    def StaffCouriersBegin(self):  # key, ip, voters in favor, admins in favor
        pass

    @OrgStaffCouriersIncrement.responder
    def StaffCouriersIncrement(self):
        pass

    @OrgStaffCouriersVerify.responder
    def StaffCouriersVerify(self):
        pass

    @OrgVolunteerCouriersBegin.responder
    # key, ip, voters in favor, admins in favor
    def VolunteerCouriersBegin(self):
        pass

    @OrgVolunteerCouriersIncrement.responder
    def VolunteerCouriersIncrement(self):
        pass

    @OrgVolunteerCouriersVerify.responder
    def VolunteerCouriersVerify(self):
        pass
    # memberships

    @OrgMembershipBegin.responder
    def MembershipBegin(self):  # membership proposal object, yea/nay-date
        pass

    @OrgMembershipIncrement.responder
    def MembershipIncrement(self):
        pass

    @OrgMembershipVerify.responder
    def MembershipVerify(self):
        pass

    @OrgProposalBegin.responder
    def ProposalBegin(self):  # proposal object, yea/nay-date
        pass

    @OrgProposalIncrement.responder
    def ProposalIncrement(self):
        pass

    @OrgProposalVerify.responder
    def ProposalVerify(self):
        pass

    @OrgVoteTallyBegin.responder
    def VoteTallyBegin(self):  # vote object, ballots cast, yea/nay-date
        pass

    @OrgVoteTallyIncrement.responder
    def VoteTallyIncrement(self):
        pass

    @OrgVoteTallyVerify.responder
    def VoteTallyVerify(self):
        pass

    @OrgPollTallyBegin.responder
    def PollTallyBegin(self):  # poll object, ballots answered, yea/nay-date
        pass

    @OrgPollTallyIncrement.responder
    def PollTallyIncrement(self):
        pass

    @OrgPollTallyVerify.responder
    def PollTallyVerify(self):
        pass

    @OrgSavesBegin.responder
    def SavesBegin(self):  # hash to save, yea/nay-date
        pass

    @OrgSavesIncrement.responder
    def SavesIncrement(self):
        pass

    @OrgSavesVerify.responder
    def SavesVerify(self):
        pass
