# Private Ballot
One of the ideas for having a vote is having a non-coerced private ballot,
which is why the end-to-end verification for Delegito does not prove you
voted in a particular way, only that your vote counted.# Creating a Jurisdiction
To create a jurisdiction, go to the "Create" tab and select "Jurisdiction".
Fill out any geographic information, the owner's public key(s), & organization bio.

Next, fill out the jurisdiction's methodology, from the number of members to
the proceedings of a vote.

# Joining a Jurisdiction
To join a jurisdiction, visit its page and select "Join". The administrators,
upon vetting you, will sign your account's public key certifying that you
are a member.

# Creating an election
To create an election, go to the create tab and select "election". If you are
not the administrator of the jurisdiction you would like to have the election
at, you must navigate to their page and "propose an election".End-User guides:

# Register to vote
Select a jurisdiction you're a voter of (see [groups](groups)).

Select any of the elections scheduled in your jurisdiction, and
after deciding if you'd like to participate, select "Register to vote".

# Casting a vote
For a public vote, rank your choices, then click submit.

If you would not like your true vote to be publicly certified,
select "vote differently than polled", and a second ballot will be displayed.

# Checking a vote
When casting your vote, you have the ability to end-to-end verify the public polls,
and that your private ballot was counted as cast. To do so, view your voting record
under your profile, if it says "ready to audit" you may select to audit your vote.

> Note: you cannot prove to anyone you voted a particular way, read more
[here](//congredi.readthedocs.io/en/latest/Methodology/zeroknowledge/).# Editing your bio
Select the gear(:gear:) from the top right corner of the UI.
Make any changes you feel necessary, then click save.

# Viewing your PGP Public Key
click the info button next to your fingerprint.


## Users / Sysadmins? [User Guide](UserGuide)
Guides involved in getting up and running with Congredi instances.

## Developers / Contributors? [API](APIs) & [Build](building) docs
Guides for getting under the hood with the overlying architecture.

## Cryptographers / Skeptics? [Methodology](methodology)
Guides for working with the underlying libraries, objects, & functions.



# Public Key

## Vetting users (certify/revoke keys)

The public key of the user, stored within the database, gets updated by
a valid certification of that user by someone else.

## Account Management (public key or fernet symetric)

Recovering account details involves using the private key on client-side
JS, without it, the account shouldn't be recoverable.

## Jurisdiction Administration (Threshold keys)

Unlocking jurisdiction options requires consent from all the parties
sharing a common secret (technically blockchain threshold sigs, not
Secure Secret Sharing, unless I can find an uncompromising method).

## Voting and elections (Shuffle-Sum)

Elections contain both a publicly signed poll ranking, and a private
shuffle-sum operation. The poll is attached to the user's profile,
while the Shuffle-Sum operation is used to verify their actual private vote.# Mongo db

