ONLY RP PLAYERS CAN CREATE GUILDS
Guilds have the ability to declare war to each other if a guild leader choses to. This changes their faction so that they can attack members of the other guild.
What needs to be done:
1. Change Unit::GetReactionTo(). This function returns a ReputationRank, so, theoretically, guilds could not only declare war, but which guilds they consider unfriendly (no aggression but no interaction either), neutral, friendly, honored, revered and exalted)
2. Allow players to have a faction based on their guild. Maybe use guild ID
3. Create a list of all existing guilds that updates every time a new one forms or an old one disbands. This list is accessible from the guild frame to all members, but only the guild leader or authorized officials can change values in it. Each row in the list represents a guild, they all have a button that opens a Frame with their info (leader, member count, description, banner, etc) and a reputation DropDownMenu, which offers the following options for GuildMasters and Officials to choose from:
(HOSTILE,UNFRIENDLY, NEUTRAL, FRIENDLY, HONORED,REVERED EXALTED)
4. GuildMasters and Officials have a unique tab in their Guild Frame that allows them to select what the different ReputationRanks can do in regards to their guild possessions. Hostile defaults to no rights, unfriendly, neutral, friendly, honored and revered are up to them and Exalted defaults to "they can do anything a guild member can". Here, they can also choose their default reaction to solo players.
5. All Guild members have a general ability that allows them to become hostile with a specific guildless player. This is to avoid rival guild players from leaving their guild to enter enemy headquarters. Also, whenever you leave a guild you become a Desertor for 1 day, disallowing you to join any other guild. Also, every day at 2 AM player guilds are registered, then held for a week. Everyone can see their last week guild history if they inspect them or look the player up in the register.


Banners: Guildmasters can submit their banner to a GameMaster in blp or png format. This must be 256x128 and be of acceptable quality (must comply with tabard rules,  be symetrical (only send half an image), no anachronisms, no bad resolution images, etc). These images will go through an approval process and, if agreed upon, added on the next update. This banners can work as the guild's tabard image, as the literal symbol of their banner, on buildings, etc...

textures/guildemblems/emblem_xx.blp // Emblem Textures mirror horizontally. 
Check Guild::HandleSetEmblem in Guild.cpp