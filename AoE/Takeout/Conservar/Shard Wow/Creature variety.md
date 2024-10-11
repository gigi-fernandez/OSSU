Creatures are created from creature templates. These are archetypes not fixed to level or special characteristics. For example, in order to make a level 17-19 Ghoul, you would base it on the "Ghoul_template", which has the type of spells the creature uses (ranked automatically for them), their stats, displayID, etc. 

Creatures, by default, don't have any AI, just associated spells with their template (Ghoul has Scratch and Inflict Plague, for example) which they use mostly at random. However, all of them have a chance of having a special AI template, which assigns them a prefix and changes their stats a bit:
- For example, an AI template that makes them kite the player will give them the prefix "Slippery", extra movement speed but lower HP. 
- There can also be AI templates that are used only for certain Creature Tags. For example, for a Scourge and Undead Beast themes, all creatures could have the "Infectious" AI, which would give them a debuff that spreads to players when struck.

These AI are also given in function of the creature's class. Mage-type creatures will have different AI than that of Warrior-type creatures.