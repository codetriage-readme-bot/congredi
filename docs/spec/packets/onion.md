Congredi uses a simplified onion-routing system to discourage some censorship.
Servers, once active on the network, ask 3 nodes to be their rendesvous, and
then sign a statement that gets advertised around the network. Clients can
make a query to those nodes through a set of layered encryptions, until
the final node and the rendesvous node, either of which may object to the query.
Since the serve stores data in plaintext, if it finds something objectionable,
or of no use, it can censor that content as well.
