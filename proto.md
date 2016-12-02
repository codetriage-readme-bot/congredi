network packets (twisted/tornado)
p2p/dht libraries

"""```
pro-self-cohesive,anti-other-coupling


relationmap, searching over shard, incentive to keep up-to-date, ranking

PSC:
    mutual-record-rumor-challenge hash-subset (optimistic) - sharding
    Send/Recieve (BASE Eventual Consistency) - update helps system
    nonce-return-pieces & incentive to provide up to date info
SHA: markdown compressed with gzip signed with ec
    - sig, ent, time, nonce
        - piece (hash+sig)
            - peer (signed hash, nonce?, date?)
    keep/delete votes ( O(1) nettrust)
VER
    bookmark-head (hash + sig + user)
    diffs (hash + sig + author)
    - subscribers who actually value that version (or children)
ENT
    - sig-denounces-last
    vers, subs, votes, groups
STV
    - sig-adds-all-known?
    person, versions, ranking, signature
AGR
    - aggregation-adds-all-group
    - group-membership-current
    STV aggregations
    membership lists


{voucher:abc,nonce:def,time:qbc,field:tc,sig:bc}
{count:10,offset:10,nonce:abc,time:abc,sig:abc,items:[],order:abc}
{count:10,offset:10,nonce:abc,time:abc,sig:abc,items:[],order:abc,field:abc}


```"""

def hello_send(): # send cleartext signed Time & Session key
    #Hello peer, my session EC is 'A', and my time is 'T', signed 'a'
def hello_get(): # check sig, send encrypted challenge nounce/time, & Session key
    #Hello, compute 'N' at my time 't', my session key is 'S', let's use 'T' signed 's'
def earn_query(): #compute nounce, send result + query, both signed
    #(encrypted T) - 'N'*'T' = 'S', Query = 'abc', sig = 'Q'
def run_result(): #check result, run query, transfer data
    #(encrypted T) - result, certification
def thank_server(): #thank the server for behaving
    #(encrypted T) - thank you, I rank you better. 'sig'
def welcome_client(): #welcome client to search again, for behaving
    #(encrypted T) - you're welcome, I rank you better for ranking me better "sig" 'sig'

def rank_welcome(): # servers who don't welcome clients (complain)
def rank_subset(): # servers who lie about storing a hash (or ask for help)
def rank_speed(): # slow send/recieve
def rank_peer_had(): # check sig of if peer had a piece (rank both/which poorly?)
def rank_01_trust():
def rank_latest_version():
def rank_denounce_accuracy():
    # send them proof they did it wrong

# rendering content
def verify_decompress_markdown():
def markdown_compress_sign():

# pieces
def piece_hash_sign():
def combine_hash_verify():
def advertise_piece():
def query_piece():

# keep/delete vote/versioning
def vote_keep_delete():
def check_01_nettrust():
def resolve_version():
def subscribe_to_versioning():

# entity
def update_denounce_summary():
def feed_objects_had(): #?
def subscribe_to_entity():
def check_denounces_last(): #duplicate?
#STV
def sig_add_all():
def check_adds_all():
def publish_ranking():
def obtain_ranking():
#AGR
def run_aggregation():
def check_aggregation():
def become_member():
def authorize_member():
def update_aggregations():
def check_aggregations():
