"""
#STV
def sig_add_all():
def check_adds_all():
def publish_ranking():
def obtain_ranking():
# keep/delete vote/versioning - O(1) is only storing what the nettrust wants
def vote_keep_delete():
def check_01_nettrust():
def resolve_version():
def subscribe_to_versioning():
# rendering content/pieces
def verify_decompress_markdown():
def markdown_compress_sign():
def piece_hash_sign():
def combine_hash_verify():
def advertise_piece():
def query_piece():
#AGR
def run_aggregation():
def check_aggregation():
def become_member():
def authorize_member():
def update_aggregations():
def check_aggregations():
# entity
def update_denounce_summary():
def feed_objects_had(): #?
def subscribe_to_entity():
def check_denounces_last(): #duplicate?
class User():
	email = "" # reset location (could be bitmessage)
	pubkey = "" # signing identity
	onion = "" # api endpoint (challenge)
	def __init__(self, email, pubkey, onion):
		self.email = email
		self.pubkey = pubkey
		self.onion = onion
		data = {'email':email,'pubkey':pubkey,'onion':onion}
		db_insert.apply_async(['users',data])
	def poll(jurisdiction,declared):
		pgp_verify(declared,self.pubkey)
		jurisdiction.has(poll) # ugh...
		data = {'pubkey':pubkey,'declared':declared}
		db_insert.apply_async(['votes',data])
	def vote(jurisdiction, chain, privvote):
		pass
class Jurisdiction():
	def __init__(self):
		pass
# complaints would be sent for not conforming
def rank_welcome(): # servers who don't welcome clients (complain)
def rank_subset(): # servers who lie about storing a hash (or ask for help)
def rank_speed(): # slow send/recieve
def rank_peer_had(): # check sig of if peer had a piece (rank both/which poorly?)
def rank_01_trust():
def rank_latest_version():
def rank_denounce_accuracy():
	# send them proof they did it wrong
{voucher:abc,nonce:def,time:qbc,field:tc,sig:bc}
{count:10,offset:10,nonce:abc,time:abc,sig:abc,items:[],order:abc}
{count:10,offset:10,nonce:abc,time:abc,sig:abc,items:[],order:abc,field:abc}
class interlocutor():
	def __init__(self, config):
		self.ec = config
	# client
	def reach():
		pass
	# server
	def greet():
		pass
# some sort of handshake would be needed (EC + fernet?) with an incentive to behave
def hello_send(): # send cleartext signed Time & Session key
	pass
	#Hello peer, my session EC is 'A', and my time is 'T', signed 'a'
def hello_get(): # check sig, send encrypted challenge nounce/time, & Session key
	pass
	#Hello, compute 'N' at my time 't', my session key is 'S', let's use 'T' signed 's'
def earn_query(): #compute nounce, send result + query, both signed
	pass
	#(encrypted T) - 'N'*'T' = 'S', Query = 'abc', sig = 'Q'
def run_result(): #check result, run query, transfer data
	pass
	#(encrypted T) - result, certification
def thank_server(): #thank the server for behaving
	pass
	#(encrypted T) - thank you, I rank you better. 'sig'
def welcome_client(): #welcome client to search again, for behaving
	pass
	#(encrypted T) - you're welcome, I rank you better for ranking me better "sig" 'sig'
"""