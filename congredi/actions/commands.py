#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP private settings. Users must be a member of the 'admin' group in storage/configs,
and must send an encrypted command request to the server.
Commands:
* Blacklist - PGP pubkeys definitely allowed to connect or issue commands.
* Whitelist - PGP pubkeys blocked from connecting or issuing commands.
* Peers - pubkeys & IP addresses of peers strongly preferred.
* Users - People we take priority in storing for (privledged get/set)
* Admins - people allowed to change these settings
Storage applies a censor policy. If they want to avoid
that policy, they'll have to ask for an encryption permit
instead.
The blacklist/whitelist should probably include IPs as well.
Proposed:
    Peer commands will match either of the values within the blacklist,
    and will track the user should one change, for instance, a block of
    a public key will add the new IP address it's seen using?
    Problem: they could be in proxy mode?
AMP passport - grant abilities to a server.
Quickly checks permissions to operate in
specific capacities.
* Storage               (proof & key-trust check)
* Encrypted Storage     (longer proof & key-trust check)
* Publish               (hidden server storing data)
* Subscribe             (hidden server looking for data)
* Rendesvous            (publish side load-balance IP)
* Courier               (subscribe side load-balance IP)
* Sanctuary             (recursive use of encrypted storage, off the books)
* Safe Passage          (permission to connect with forwardable packets)
Permissions are granted/lost on:
* Behavior
* Manual Overide
* Key Trust Depth
* Server Load
Could possibly introduce rate limits?
AMP filesystem operations
Bulk Operations:
* SyncHavesWants        - send a list of hashes, recieve a list of hashes
New Bulk Operation:
* SyncStorage           - send a list of blobs, recieve a list of blobs
These are the user properties.
Smaller, previous non-bulk operations:
* StoreSet              - basic Redis operations...
* EncryptedStoreSet
* StoreGet
* EncryptedStoreGet
* Seek                  - send hashes by keyspace offset (hash, number, direction)
* Resolve               - not documented yet. Part of periodic tasks, http iface
* Search                - will not work on encrypted stores
AMP command tests
Orgs are collections of people who make decisions
after a threshold of consensus. When new admins are
added, the org keys fundimentally change hands.
Operations involving adding or removing citizens,
however, occur under the existing keys.
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, ListOf, Boolean, DateTime, String, Integer
from ..commits.diffs import resolveDiff
from ..utils.errors import CongrediError
from .objects import EncAddress, EncHash, EncBool, EncSig, PrivAES, EncBlob
from .objects import ObjAddress, ObjHash, ObjSig, ObjBlob, ObjPubKey
# addresses
# blockable pubkeys
class UserUpdate(Command):
    # arguments = [(b'name', String()),
    #              (b'port', Integer())]
    # response = [(b'hello', String())]
    response = []
    """
    new public key, previous one signing it
    """
class UserSync(Command):
    response = []
class UserBioUpdate(Command):  # blob, previous hash, sig
    response = []
class UserBioSync(Command):
    response = []
class UserLocationUpdate(Command):  # zkp, previous hash, sig
    response = []
class UserLocationSync(Command):
    response = []
class UserCourierUpdate(Command):  # fingerprint, ip, previous hash, sig
    response = []
class UserCourierSync(Command):
    response = []
class UserRendesvousUpdate(Command):  # fingerprint, ip, previous hash, sig
    response = []
class UserRendesvousSync(Command):
    response = []
class UserReqJoinUpdate(Command):  # org fingerprints summary, previous hash, sig
    response = []
class UserReqJoinSync(Command):
    response = []
# org fingerprints summary, commit hash, vote object, previous, sig
class UserProposalUpdate(Command):
    response = []
class UserProposalSync(Command):
    response = []
# org fingerprints summary, proof of membership, previous, sig
class UserMembershipUpdate(Command):
    response = []
class UserMembershipSync(Command):
    response = []
# the vote, my ballot, previous hash, sig
class UserCastedVotesUpdate(Command):
    response = []
class UserCastedVotesSync(Command):
    response = []
# hash of the starting commit, commit blob, previous hash, sig
class UserTreeUpdate(Command):
    response = []
class UserTreeSync(Command):
    response = []
class UserSavesUpdate(Command):  # hash to save, previous saves hash, sig
    response = []
class UserSavesSync(Command):
    response = []
class userResponders(object):
    redis = None
    neo4j = None
    def __init__(self):
        # would pulll Redis online
        pass
    @UserUpdate.responder
    def Update(self):
        # arguments = [(b'name', String()),
        #              (b'port', Integer())]
        # response = [(b'hello', String())]
        """
        new public key, previous one signing it
        """
        # checkPreviousKeySignsNewOne()
        userKeyFingerprint = b'TBD'
        userKey = b'TBD'
        self.redis.write(b'users:' + userKeyFingerprint, userKey)
        return True
    @UserSync.responder
    def Sync(self):
        pass
    @UserBioUpdate.responder
    def BioUpdate(self):  # blob, previous hash, sig
        pass
    @UserBioSync.responder
    def BioSync(self):
        pass
    @UserLocationUpdate.responder
    def LocationUpdate(self):  # zkp, previous hash, sig
        pass
    @UserLocationSync.responder
    def LocationSync(self):
        pass
    @UserCourierUpdate.responder
    def CourierUpdate(self):  # fingerprint, ip, previous hash, sig
        pass
    @UserCourierSync.responder
    def CourierSync(self):
        pass
    @UserRendesvousUpdate.responder
    def RendesvousUpdate(self):  # fingerprint, ip, previous hash, sig
        pass
    @UserRendesvousSync.responder
    def RendesvousSync(self):
        pass
    @UserReqJoinUpdate.responder
    def ReqJoinUpdate(self):  # org fingerprints summary, previous hash, sig
        pass
    @UserReqJoinSync.responder
    def ReqJoinSync(self):
        pass
    @UserProposalUpdate.responder
    # org fingerprints summary, commit hash, vote object, previous, sig
    def ProposalUpdate(self):
        pass
    @UserProposalSync.responder
    def ProposalSync(self):
        pass
    @UserMembershipUpdate.responder
    # org fingerprints summary, proof of membership, previous, sig
    def MembershipUpdate(self):
        pass
    @UserMembershipSync.responder
    def MembershipSync(self):
        pass
    @UserCastedVotesUpdate.responder
    def CastedVotesUpdate(self):  # the vote, my ballot, previous hash, sig
        pass
    @UserCastedVotesSync.responder
    def CastedVotesSync(self):
        pass
    @UserTreeUpdate.responder
    def TreeUpdate(self):  # hash of the starting commit, commit blob, previous hash, sig
        pass
    @UserTreeSync.responder
    def TreeSync(self):
        pass
    @UserSavesUpdate.responder
    def SavesUpdate(self):  # hash to save, previous saves hash, sig
        pass
    @UserSavesSync.responder
    def SavesSync(self):
        pass
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
class ErrNoPrevious(CongrediError):
    pass
class ErrIncompleteListing(CongrediError):
    pass
# union operation (data transfer)
class SyncHavesWantsAsk(Command):
    arguments = [(b'have', ListOf(ObjHash)),
                 (b'want', ListOf(ObjHash))]
    # should be providing auths
    Responses = [(b'have', ListOf(ObjHash)),
                 (b'want', ListOf(ObjHash))]
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """
# union operation (data transfer)
class SyncStorageAsk(Command):
    arguments = [(b'blobs', ListOf(ObjBlob))]
    # should be providing auths
    Responses = [(b'blobs', ListOf(ObjBlob))]
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """
# store object (encrypted or not)
class StoreSet(Command):
    """
    Adding a key (permissioned, recursive)
    Adding a key (permissionless, non-recursive)
    """
    """
    sends: object
    recieves: lifetime, signature
    PUBLISH TYPE foobar HASH abc AUTHOR author OBJECT object SIGNATURE sig
    [ 2016-10-11 20:10:10, signature ]
    sends: object
    recieves: lifetime, signature
    DEPLOY TYPE foobar HASH abc AUTHOR author OBJECT object SIGNATURE sig
    [ 2016-10-11 20:10:10, signature ]
    """
    arguments = [(b'author', String()),
                 # permissioned + recursive || permissionless + unrecursive
                 (b'authority', Boolean()),
                 (b'hash', String()),
                 (b'signature', String()),
                 (b'object', String()),
                 (b'type', String())
                 ]
    response = [
        (b'lifetime', DateTime()),
        (b'signature', String())]
    arguments = [(b'blob', ObjBlob()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'done', Boolean()),
                 (b'ttl', DateTime())]
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
class EncryptedStoreSet(Command):
    arguments = [(b'blob', ObjBlob()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'done', Boolean()),
                 (b'ttl', DateTime())]
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
# get object (encrypted or not)
class StoreGet(Command):
    """
    Geting a key (permissioned, recursive)
    Geting a key (permissionless, non-recursive)
    """
    """
    MONITOR TYPE foobar HASH hash READER reader SIGNATURE sig
    [ Results[], 2016-10-11 20:10:10, signature ]
    SUBSCRIBE TYPE foobar HASH hash READER reader SIGNATURE sig
    [ Results[], 2016-10-11 20:10:10, signature ]
    """
    arguments = [(b'reader', String()),
                 # permissioned + recursive || permissionless + unrecursive
                 (b'authority', Boolean()),
                 (b'hash', String()),
                 (b'signature', String()),
                 (b'object', String()),
                 (b'type', String())
                 ]
    response = [
        (b'lifetime', DateTime()),
        (b'signature', String())]
    arguments = [(b'hash', ObjHash()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'blob', ObjBlob()),
                 (b'ttl', DateTime())]
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
class EncryptedStoreGet(Command):
    arguments = [(b'hash', ObjHash()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'blob', ObjBlob()),
                 (b'ttl', DateTime())]
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
# seek item ([hash]->num)
class SeekGet(Command):
    """
    Grab starting at a hash and moving backwards, with an offset and object count
    Grab starting at a hash and moving forward on the list, with an offset and object count
    Grab from the latest of the list, with an offset and object count
    """
    """
    type : hash : [list]
    foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]
    GET PAST foo stu OFFSET 1 COUNT 3
    GET FUTURE foo ghi OFFSET 2 COUNT 2
    GET CURRENT foo bar OFFSET 5 COUNT 2
    """
    arguments = [(b'type', String()),
                 (b'direction', String()),  # Forward || reverse
                 (b'hash', String()),  # hash || "latest"
                 (b'offset', Integer()),
                 (b'count', Integer())]
    response = [(b'hashes', String())]  # list of strings...
    arguments = [(b'keyspace', ObjHash()),
                 (b'count', Integer()),
                 (b'forward', Boolean())]
    # should be providing auths
    Responses = [(b'hashes', ListOf(ObjHash()))]
    """
    'seek hashes key [hash] count [number] direction [+/-]'
    I: hash, number, direction
    O: list of hashes
    """
# resolve item ([hash])
# ?? might simply do 'send me the blobs'...
class ResolveGet(Command):
    arguments = [(b'hash', ObjHash())]
    # should be providing auths
    Responses = [(b'blob', ObjBlob())]
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
# search items
class SearchRun(Command):
    """
    Search from content-containing objects
    """
    """
    type : hash : [list]
    foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]
    GET SEARCH foo TERM "cats" OFFSET 10 COUNT 100
    [ bar, otherbar ]
    """
    arguments = [(b'type', String()),
                 (b'term', String()),
                 (b'offset', Integer()),
                 (b'count', Integer())]
    # response = [(b'hashes', String())]  # list of strings...
    arguments = [(b'hash', ObjHash()),
                 (b'type', String())]
    # should be providing auths
    responses = [(b'blob', ObjBlob()),
                 (b'ttl', DateTime())]
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
class filesystemResponders(object):
    redis = None
    neo4j = None
    def __init__(self, givenRedis):
        self.redis = givenRedis
    @SyncHavesWantsAsk.responder
    def SyncHavesWantsTell(self, peerName, yourWants, yourHaves):
        """
        'I have [x,y,z], I want [x,y,z], what do you have/want'
        I: list of hashes, list of hashes
        O: list of hashes, list of hashes
        """
        myWants = self.redis.read(b'wants')
        myHaves = self.redis.read(b'haves')
        self.redis.write(b'peer:wantsof:' + peerName, yourWants)
        self.redis.write(b'peer:havesof:' + peerName, yourHaves)
        return myWants, myHaves
    @SyncStorageAsk.responder
    def SyncStorageTell(self, yourBlobs, yourRequests):
        """
        'I have [x,y,z], I want [x,y,z], what do you have/want'
        I: list of hashes, list of hashes
        O: list of hashes, list of hashes
        """
        results = {}
        for request in yourRequests:
            results[request] = self.redis.read(request)
        self.redis.write(b'blobs', yourBlobs)
        # generateWants?
        #wants = self.redis.read(b'wants')
        return results  # , wants
    @StoreSet.responder
    def StoreSetConfirm(self, blob, typeOf, author, sig):
        """
        'store blob [blob] of type [type]'
        I: blob, type
        O: bool, ttl
        """
        # checksig(sig)
        # checkPermissionForStorage()
        self.redis.write(blob)
        ttl = b'TBD'
        return True, ttl
    @EncryptedStoreSet.responder
    def EncryptedStoreSetConfirm(self, blob, typeOf, author, sig):
        """
        'store blob [blob] of type [type]'
        I: blob, type
        O: bool, ttl
        """
        # if checksig(sig)
        # if checkPermissionForEncryption()
        self.redis.write(blob)
        ttl = b'TBD'
        return True, ttl
    @StoreGet.responder
    def StoreGetRespond(self, keys, typeOf, author, sig):
        """
        'send blob [blob] of type [type]'
        I: list of hashes, type
        O: list of blobs, ttl
        """
        results = {}
        for request in keys:
            # sql escape on this keyspace...
            results[request] = self.redis.read(typeOf, request)
        ttl = b'TBD'
        return results, ttl
    @EncryptedStoreGet.responder
    def EncryptedStoreGetRespond(self, keys, typeOf, author, sig):
        """
        'send blob [blob] of type [type]'
        I: list of hashes, type
        O: list of blobs, ttl
        """
        # checkReadPermission()
        results = {}
        for request in keys:
            # sql escape...
            results[request] = self.redis.read(typeOf, request)
        ttl = b'TBD'
        return results, ttl
    @SeekGet.responder
    def SeekRespond(self, key, count, direction):
        """
        'seek hashes key [hash] count [number] direction [+/-]'
        I: hash, number, direction
        O: list of hashes
        """
        result = []
        current = key
        seek = b'next:'
        if direction == True:
            seek = b'previous:'
        try:
            # pylint: disable=unused-variable
            for c in count:
                nextKey = self.redis.read(seek + current)
                result.append(nextKey)
                current = nextKey
        # pylint: disable=bare-except
        except:
            if len(result) == 0:
                return ErrNoPrevious()
            return ErrIncompleteListing()
        return result
        # pylint: disable=bare-except
    @ResolveGet.responder
    def ResolveRespond(self, keyhash, typeOf):
        """
        'resolve [hash]'
        I: hash
        O: blob
        """
        # check if that resolve exists?
        # findFirst()
        current = keyhash.first()
        keyHashList = []
        for modification in keyHashList:
            current = resolveDiff(current, modification)
        self.redis.write(b'resolved:' + keyhash, current)
        return current
    @SearchRun.responder
    def SearchRespond(self, keyspace, term):
        """
        'resolve [hash]'
        I: hash
        O: blob
        """
        regex = term
        results = []
        for keys in keyspace:
            key = self.redis.read(keys)
            lookup = regex(key)
            results.append(lookup)
        return results
class AddrGet(Command):
    # arguments = [(b'name', String()),
    #              (b'port', Integer())]
    # response = [(b'hello', String())]
    response = []
    """
    'what is the address of the key [x]'
    I: key
    O: string
    """
class CensorPolicyGet(Command):
    """
    'what is the censor policy of the key [x]'
    I: key
    O: string
    """
# ranks
class RankGet(Command):
    """
    'what is the rank of the key [x]'
    I: key
    O: string
    """
class SeenGet(Command):
    """
    'when was key [x] last seen'
    I: key
    O: string
    """
class UptimeGet(Command):
    """
    'what is the uptime of key [x]'
    I: key
    O: string
    """
# haves/wants
class WantsGet(Command):
    """
    'what does key [x] want'
    I: key
    O: list of hashes
    """
class HasGet(Command):
    """
    'what does key [x] have'
    I: key
    O: list of hashes
    """
class ProofGet(Command):
    """
    'prove key [x] has [hash] section[:] with [nonce]'
    I: key, hash, start, end, nonce
    O: proof
    """
# publish functions
class RendesvousGet(Command):
    """
    'rendesvous of key [x]'
    I: key
    O: of, by
    """
class CourierGet(Command):
    """
    'courier of key [x]'
    I: key
    O: of, by
    """
class routerResponders(object):
    redis = None
    neo4j = None
    def __init__(self):
        # would pulll Redis online
        pass
    @AddrGet.responder
    def GetAddr(self, ):
        """
        'what is the address of the key [x]'
        I: key
        O: string
        """
        pass
    @CensorPolicyGet.responder
    def GetCensorPolicy(self, ):
        """
        'what is the censor policy of the key [x]'
        I: key
        O: string
        """
        pass
    @RankGet.responder
    def GetRank(self, ):
        """
        'what is the rank of the key [x]'
        I: key
        O: string
        """
        pass
    @SeenGet.responder
    def GetSeen(self, ):
        """
        'when was key [x] last seen'
        I: key
        O: string
        """
        pass
    @UptimeGet.responder
    def GetUptime(self, ):
        """
        'what is the uptime of key [x]'
        I: key
        O: string
        """
        pass
    @WantsGet.responder
    def GetWants(self, ):
        """
        'what does key [x] want'
        I: key
        O: list of hashes
        """
        pass
    @HasGet.responder
    def GetHas(self, ):
        """
        'what does key [x] have'
        I: key
        O: list of hashes
        """
        pass
    @ProofGet.responder
    def GetProof(self, ):
        """
        'prove key [x] has [hash] section[:] with [nonce]'
        I: key, hash, start, end, nonce
        O: proof
        """
        pass
    @RendesvousGet.responder
    def GetRendesvous(self, ):
        """
        'rendesvous of key [x]'
        I: key
        O: of, by
        """
        pass
    @CourierGet.responder
    def GetCourier(self, ):
        """
        'courier of key [x]'
        I: key
        O: of, by
        """
        pass
class PrivateBlacklistChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    Sign & Encrypt Action
        - encrypt for the TO field.
    Create Integrity Data
        - sign with external key
        Check Integrity data (sesh hash/sig)
        - must be signed with FROM field
        Check Signature for action
            - must be in Admins keyspace
        Perform Action
            - Remove from blacklist.
        Return Response (encrypted, signed)
    Check Integrity Data
        - must be from TO field
    Check Encrypted Signature
        - must be from your server
    """
class PrivateBlacklistView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted blacklist, encrypted sig
    """
class PrivateWhitelistChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted signed response, encrypted hash, hash
    """
class PrivateWhitelistView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
# peers
class PrivatePeersChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted whitelist
    """
class PrivatePeersView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
# users/admins
class PrivateUsersChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
class PrivateUsersView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
class PrivateAdminsChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
class PrivateAdminsView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
class settingResponders(object):
    config = None
    redis = None
    neo4j = None
    def __init__(self, givenRedis):
        self.redis = givenRedis
    # blacklist
    @PrivateBlacklistChange.responder
    def ChangePrivateBlacklist(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            self.redis.write(b'blacklist', address)
            return True
        return False
    @PrivateBlacklistView.responder
    def ViewPrivateBlacklist(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            blacklist = self.redis.read(b'blacklist')
            return blacklist
        return False
    # whitelist
    @PrivateWhitelistChange.responder
    def ChangePrivateWhitelist(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            self.redis.write(b'whitelist', address)
            return True
        return False
    @PrivateWhitelistView.responder
    def ViewPrivateWhitelist(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            whitelist = self.redis.read(b'whitelist')
            return whitelist
        return False
    # peers
    @PrivatePeersChange.responder
    def ChangePrivatePeers(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            self.redis.write(b'peers', address)
            return True
        return False
    @PrivatePeersView.responder
    def ViewPrivatePeers(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            peers = self.redis.read(b'peers')
            return peers
        return False
    # users
    @PrivateUsersChange.responder
    def ChangePrivateUsers(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            self.redis.write(b'users', address)
            return True
        return False
    @PrivateUsersView.responder
    def ViewPrivateUsers(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            users = self.redis.read(b'users')
            return users
        return False
    # admins
    @PrivateAdminsChange.responder
    def ChangePrivateAdmins(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            self.redis.write(b'admins', address)
            return True
        return False
    @PrivateAdminsView.responder
    def ViewPrivateAdmins(self, pubkey, address, direction):
        if pubkey in self.redis.read(b'admins'):
            admins = self.redis.read(b'admins')
            return admins
        return False
class StoreRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# PubKey, TTL -> Boolean, TTL
"""
Encrypted storage applies an inverted sensor. It better
look like it's ben tripleSec encrypted, and we'll do it
again to keep the storage provider from indexing it.
"""
class StoreEncryptedRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# private servers acting as publisher (permissioned or not)
"""
As a private server, a user will connect to them to find any
new content. This is where the actual data sits, if in
strict encryption mode. Otherwise, the rendesvous & courier
may be allowed to cache the request.
"""
class PublishRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
class SubscribeRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# private servers acting as rendesvous to a server
"""
The Rendesvous (or publishing) and Courier (or subscribing)
relays are public addresses that speak on behalf of a server.
"""
class RendesvousRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
class CourierRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# onion network / onion storage
"""
Sanctuary is an unlisted, encrypted server that
backs up, encrypted, to other servers. Safe Passage
is the permission to act as a tor-like relay
"""
class SanctuaryRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
class SafePassageRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
class passportResponders(object):
    redis = None
    neo4j = None
    def __init__(self, GivenRedis, GivenNeo4j):
        # would pull Neo4j online
        self.redis = GivenRedis
        self.neo4j = GivenNeo4j
    @StoreRequest.responder
    def StoreGrant(self, pubkey, ttl):
        """
        Compute
        """
        # somehow store TTL?
        if self.neo4j.TrustWithin(3):
            self.redis.write(b'permissions:store', pubkey)
        signedStorage = b'TBD'
        ttl = b'TBD'
        return signedStorage, ttl
    @StoreEncryptedRequest.responder
    def StoreEncryptedGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(2):
            self.redis.write(b'permissions:storeEncrypted', pubkey)
        signedStorage = b'TBD'
        ttl = b'TBD'
        return signedStorage, ttl
    @PublishRequest.responder
    def PublishGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(3):
            self.redis.write(b'permissions:publish', pubkey)
        signedPublish = b'TBD'
        ttl = b'TBD'
        return signedPublish, ttl
    @SubscribeRequest.responder
    def SubscribeGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(2):
            self.redis.write(b'permissions:subscribe', pubkey)
        signedSubscribe = b'TBD'
        ttl = b'TBD'
        return signedSubscribe, ttl
    @RendesvousRequest.responder
    def RendesvousGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'rendesvous', pubkey)
        signedRendesvous = b'TBD'
        ttl = b'TBD'
        return signedRendesvous, ttl
    @CourierRequest.responder
    def CourierGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'courier', pubkey)
        signedCourier = b'TBD'
        ttl = b'TBD'
        return signedCourier, ttl
    @SanctuaryRequest.responder
    def SanctuaryGrant(self, pubkey):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'permissions:sanctuary', pubkey)
        signedSanctuary = b'TBD'
        ttl = b'TBD'
        return signedSanctuary, ttl
    @SafePassageRequest.responder
    def SafePassageGrant(self, pubkey):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'permissions:onion', pubkey)
        signedSafePassage = b'TBD'
        ttl = b'TBD'
        return signedSafePassage, ttl
# find address from outside
# set this on a timer in klein instance
# ping/pong
class AddressAsk(Command):
    arguments = [(b'name', ObjAddress()),
                 (b'port', Integer())]
    response = [(b'name', ObjAddress()),
                (b'port', Integer())]
class SyncPeerDirectoryAsk(Command):
    # would have prefered dict capability.
    # these may need encoding...
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    def __init__(self, commandType, *a, **kw):
        print('Command Created')
        super(SyncPeerDirectoryAsk).__init__(commandType, *a, **kw)
    """
    in: list((key,ip))
    out: list((key,ip))
    """
# rendesvous/courriers
class SyncRendesvousDirectoryAsk(Command):
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    """
    in: list((key, rendesvous key, proof))
    out: list((key, rendesvous key, proof))
    """
class SyncCourierDirectoryAsk(Command):
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    """
    in: list((key, courier key, proof))
    out: list((key, courier key, proof))
    """
class addressesResponders(object):
    redis = None
    neo4j = None
    def __init__(self, givenRedis):
        self.redis = givenRedis
    @AddressAsk.responder
    def AddressTell(self):
        """
        Add that person to the ephemeral recently-seen list.
        Send back what their IP/port was.
        """
        myAddress = self.redis.read(b'self:addr')
        return myAddress
    # ask the directory, while sending your own
    @SyncPeerDirectoryAsk.responder
    # yourPeers):
    def SyncPeerDirectoryTell(self, dir_pubkey, dir_addrs, dir_ports):
        """
        in: list((key,ip))
        out: list((key,ip))
        """
        # logger.info('HELLOPWE')
        print('SyncPeerDirectoryAsk')
        # myPeers
        dir_addrs = self.redis.read(b'list:peers')
        # self.redis.write(b'todo:peers', yourPeers)
        return dir_pubkey, dir_addrs, dir_ports
        # return myPeers
    @SyncRendesvousDirectoryAsk.responder
    def SyncRendesvousDirectoryTell(self, yourRendesvous):
        """
        in: list((key, rendesvous key, proof))
        out: list((key, rendesvous key, proof))
        """
        myRendesvous = self.redis.read(b'list:rendesvous')
        self.redis.write(b'todo:rendesvous', yourRendesvous)
        return myRendesvous
    @SyncCourierDirectoryAsk.responder
    def SyncCourierDirectoryTell(self, yourCouriers):
        myCouriers = self.redis.read(b'list:couriers')
        self.redis.write(b'todo:couriers', yourCouriers)
        return myCouriers
class CongrediAPI():
    commandKeys = []
    defaultHost='abcdREPLACE'
    def __init__(self, host=defaultHost, port=4400, redisDetails=6379, neo4jDetails=7474, initialKey=None):
        self.host = host
        self.port = port
        self.redisDetails = redisDetails
        self.neo4jDetails = neo4jDetails
        if initialKey:
            self.commandKeys.append(initialKey)
        # ReminderToPing = task.LoopingCall(self.ping).start(15.0)
        # reactor.add(ReminderToPing)
    def ping(self):
        peerlist = self.redis.get('peerlist')
        for peer in peerlist:
            SyncPeerDirectoryAsk(peer)
#
