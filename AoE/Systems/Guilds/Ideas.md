Caravans: Caravans are mobile vehicles used to transport large quantities of goods between cities, addressing the limitations of player storage. Key features include:

1. Capacity: Can carry significantly more items than individual players.
2. Routes: Travel along predetermined paths between major cities and guild territories.
3. Vulnerability: Can be attacked by NPCs (bandits) or hostile players during transit.
4. Escort system: Players can accompany caravans for protection, earning rewards.
5. Guild management: Guilds can own and operate caravans, scheduling routes and cargo.
6. Risk vs. Reward: Successful deliveries yield profits, while losses can be substantial.
7. Economy impact: Caravans influence market prices and resource availability in different regions.
8. Upgrades: Guilds can invest in improving caravan speed, capacity, or defenses.
9. Events: Occasional special events centered around high-value caravans or dangerous routes.
Caravans add depth to the game's economy and create opportunities for PvP and PvE content.

Storage system: Anything can have an inventory, and inventories can be accessed through a storage interface. NPCs, objects, etc. This is crucial for the caravan system.

Guild Territory: Guilds can conquer territory, which allows them to use the terrain for lots of different purposses. Guild Leaders can also set the name of their territories. This name will be displayed everywhere in the interface (On top of minimap, on enter area, etc) DB Table: AreaID, GuildID, AreaName.

Guild Reputation: Guilds can declare the reaction state of their members towards members of other guilds and factions. This reaction state determines how guild members interact with others in the game world. Possible reaction states could include friendly, neutral, or hostile. When two guilds have different reaction states towards each other, the more aggressive state takes precedence. For example, if Guild A declares a friendly state towards Guild B, but Guild B declares a hostile state towards Guild A, the hostile state will be enforced for interactions between members of these guilds. This system allows for complex inter-guild relationships and potential conflicts, adding depth to the social and political aspects of the game.

Territory Conquest: [Link to ./conquest](./conquest). Guilds can conquer each other's territory. The territory is split in Areas the size of a quarter ADT or so. To conquer a certain Area, the assaulting guild must declare its intention to attack that territory, which sends a timed warning to the defendant (12 hours). The siege starts either when both parts agree or when the timer runs out. Last guild standing wins, and players who've died cannot rejoin the battle. If and once the territory is conquered, the victors can't use the zone until 12 hours pass (as to give the opportunity of a counterattack) or, in case the losing guild decides to counterattack before that time passes, until they defeat the previously defendant again. Whoever may win in that manner has a period of grace where they can use all the territories' features without interjection from the defeated guild. Guilds can form alliances to attack or defend the territory, and outsider guilds can't interact with contestants as long as the siege lasts.

Territory Map: All territories appear divided in a map. If you hover your mouse over a territory, info appears, like level of development, controlling guild, etc.

Guild Infrastructure: Guilds can build things like buildings, roads, etc. in their territory. GMs and Officers have an AIO pannel that lets them see buildings, their info, resources needed, etc. If they have the resources, they can order their construction. Following the order, they receive an item that summons a marker on the desired spot for the center of the building, in exchange for said resources. These IS have a construction time, and when they are close to completion, the marker signals GMs to add the model in noggit. 

Guild Signs: Gameobjects that hold a player's message. These can be placed anywhere on the guild's terrain by authorized guild members, and can always be removed by Guild Leaders or Officers. DB Table: GameObjectGUID, PlayerGuild, PlayerRank, Message. 

Guild Special Permissions: It defines what can players do based on rank. There's a list of permissions and Leaders decide which Ranks can do what. DB Table: GuildID, RankID, Permission (permission is an enum).

Guild NPCs: GMs and Officials can hire different NPCs in cities. They fill different roles and have different needs (different foods, infrastructure, other NPCs, etc). Also, big NPCs take some time to reach the battleground. For example, dragons only arrive to the battle after 20 minutes have passed, while footsoldiers are there from the beggining.