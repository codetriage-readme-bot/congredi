# Angular UI designs
> Think Hoodiecrow/mailvelope/whiteout-io/mailpile

Congredi needs a UI, and the one I can think of is a staticly
served Angular app. This would aquire a JWT for a flask API,
with OpenPGPjs (I don't think we have EC/Fernet) to send/recieve
data to humans.

The serving is contained over at [loading](loading)


```
    /#/
	.when('/', {
	.when('/auth', {
	.when('/settings', {
	.when('/search', {
	.when('/create', {
	.when('/edit', {
	.when('/points:id', {
	.otherwise({
		redirectTo: '/'
	});
```
```
/api/
	/auth/          [POST|DELETE] - db
	/token/         [GET|DELETE] - JWT
	/bearing/       [GET|DELETE] - JWT (longer time)

	/<user>/
		/trust/ - update your pgp keys
		/avatar/ - png/jpeg avatar
		/profile/ - json dict profile strings
		/<user>/ - return user dict
			/avatar/ - return user image
			/trust/ - sign their key with yours
	/search/ - return key:value from a value search
		{ type:["~"|"<"|">"|"=="], amount:int, offset: int, subset: "key", search: "string" }
		{ meta:{offset:int,amount:int}, key: base64, value: { json } }
		/peers/ - /peer/ indexes, some meta searches
		/govts/
		/votes/
		/options/
/peer/ - return idx
	/<hash>/ - current onion addresses
		/trust/ - pgp key chain
		/uptime/ - reputation
		/stake/ - stake proof blocks
/govt/ - return idx
	/<jurisdiction>/ - return active vote/user blocks (signed by jurisdiction)
		/validated/ - issues signed on by consensus (multiple winners)
		/ordered/ - distributed block (data secure)
		/unordered/ - idx proposed issues
		/denied/ - idx of issues denied entrance
		/<issueid>/ - return an issue signature
/vote/ - return idx
	/<hash>/ - genesis block
		/validated/ - idx of asserted
		/ordered/ - idx of consensus-ordered
		/unordered/ - idx of proposed blocks
		/open/ - idx of voters who have not voted
		/<blockid>/ - return a block and its contents
```
# Auth
* URL: `/api/auth/`

## Registering
* Format: **POST**
* Data: `{ username:'username',password:'hashed',email:'email'}`
* Results: `{Authoriation: aldkfj}`

## Canceling
* Format: **DELETE**
* Data: ``
* Results: `{goodbye:'for now'}`

# Token
Heartbeat tokens for faster endpoints
* URL: `/api/token/`
* Format: **GET**/**DELETE**
* Data:
* Results:

# Bearing
Oauth token for longer storage
* URL: `/api/bearing/`
* Format: **GET**/**DELETE**

# Search
Data queries
* URL: `/api/search/:type?offset=0?limit=0`
* Format: **GET**
* Data: {term:"",author:""}
* Results:

```
/#/
    /auth/ -> login hover
    /settings/ -> item number
    /create/ -> district,election,point
    /:user/ -> follow,message
    /:district/ -> join
        /admin
        /:election/ -> register,vote,audio
```
# Home `/#/`
* src: [interface/views/home.html](//github.com/thetoxicarcade/congredi/interface/views/home.html)


# Login Hover `/#/auth/`
* src: [interface/views/auth.html](//github.com/thetoxicarcade/congredi/interface/views/auth.html)


# Settings Bulletin `/#/settings/`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)


# Create page `/#/create/`
* src: [interface/views/create.html](//github.com/thetoxicarcade/congredi/interface/views/create.html)


# User page `/#/:user/`
* src: [interface/views/user.html](//github.com/thetoxicarcade/congredi/interface/views/user.html)


# District page `/#/:district/`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)


# District Admin page `/#/:district/admin`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)


# Election page `/#/:district/:election/`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)


## Edits to Angular UI js

1. run `gulp clean`
2. make edits to `/js/`
    * if you change a library call, change its `.test.js`
    * if you change a controller or otherwise, change its `view`
3. run `gulp` (should run tests as well)
