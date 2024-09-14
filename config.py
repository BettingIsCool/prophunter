TABLE_BETS = 'prophunter'


# Display text om landing page
TEXT_LANDING_PAGE = """

### YOUR DAILY DOSE OF PROP BETS FOR NFL, NBA, NHL, MLB 🏈🏀🏒⚾️

⭐️ All bets listed in an easy-to-consume dashboard.

⭐️ Support for 75 different prop markets!

⭐️ Many bookmakers supported (see list below).

⭐️ Apply filters and only list bookmakers & leagues that you are interested in.

⭐️ Set minimum value threshold.

⭐️ Algorithm built on @12Xpert‘s robust #WisdomOfTheCrowd strategy.

⭐️ Fair odds included. This allows you to check for value at other bookmakers as well.

👇 List of supported bookmakers 👇

##### 🇺🇸 US Bookmakers
BetOnline.ag, BetMGM, BetRivers, BetUS, Bovada, DraftKings, FanDuel, LowVig.ag, MyBookie.ag, PointsBet (US), SuperBook, Unibet, William Hill (Caesars), WynnBET, betPARX, ESPN BET, Fliff, Hard Rock Bet, SI Sportsbook, Tipico, Wind Creek (Betfred PA)

##### 🇬🇧 UK Bookmakers
888sport, Betfair Exchange, Betfair Sportsbook, Bet Victor, Betway, BoyleSports, Casumo, Coral, Grosvenor, Ladbrokes, LeoVegas (Unibet), LiveScore Bet, Matchbook, Mr Green (Unibet), Paddy Power, Sky Bet, Unibet, Virgin Bet, William Hill (UK)

##### 🇪🇺 EU Bookmakers
1xBet, 888sport, Betclic, Betfair Exchange, BetOnline.ag, Betsson, Bet Victor, Coolbet, Everygame, Livescorebet (EU), Marathon Bet, Matchbook, MyBookie.ag, NordicBet, Suprabets, Unibet, William Hill

##### 🇦🇺 AU Bookmakers
Betfair Exchange, BlueBet, Ladbrokes, Neds, PlayUp, PointsBet (AU), SportsBet, TAB, TopSport, Unibet

"""

TEXT_BEST_PRACTICE = """

#### BEST PRACTICE & SOME RECOMMENDATIONS

👉 Slide the 'Min Value Percentage' to whatever value you like, basically anything above 0% is good. If you want more bets, lower the value - if you aim for a higher ROI (less bets) then set min_val to 5%+ (or even more). The number of bets/ROI obviously also depend on your book and by how much their pricings deviate from the market.

👉 Be especially wary of potentially very high value bets, i.e. 15% and above. The source of odds is an api which is usually reliable & fast enough, but can have delays. Since this is a 3rd party api there is nothing I can do about it. You have two options to tackle this problem

(1) Head over to https://betstamp.app and verify the reference odds. Pinnacle odds (those you see in the betstamp app) must match (or be very close) to 'REF_ODDS' in the table. If Pinnacle odds are significantly higher then you might want to skip the bet.

(2) Verifying odds (1) is time consuming. You can skip this process and just place the bet, however understand that sometimes this might result in a -ev bet. At the same time it's not make-or-break if you occasionally make a -ev bet as long as the vast majority of your bets is +ev. It's really a trade off between your time & roi. I personally rarely verify the odds as it's just too much hassle for me.

👉 Timing the bets is not that big of an issue really. I personally check the dashboard multiple times a day and fire the bets in. I tend to check MLB/NBA/NHL games more often closer to kickoff, but place NFL bets throughout the week even a couple of days before kickoff.

👉 I recommend registering your bets at https://betstamp.app (I don't have a deal with them just in case you are wondering). You can follow your bets with live updates and it really makes for a great user experience especially on a busy day with multiple bets on the line.

👉 If your book of choice is not listed then there are many mirror sites (clones) that you could reference, i.e. unibet has the same odds as 888/mgreen/leovegas. From what I know ceasars (us) has the same odds as william hill, etc. so it's often just about finding out which US/EU/UK books are using the same odds.

👉 If you see a book in the list of supported bookmakers (front page), it's still possible that no bets come through. This means that either there are currently no value bets or that the api does not support prop markets for the selected book yet. However coverage is expanding, hence support for new bookmakers and prop markets for existing bookmakers will be added in future releases.

GOOD LUCK and enjoy your betting!

"""
