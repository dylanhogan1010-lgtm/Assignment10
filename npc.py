class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

NPCS = {
    "Elder Martin": NPC("Elder Martin", "Welcome traveler! Our village is threatened by monsters in the Dark Forest. Find the portal key!"),
    "Blacksmith Boris": NPC("Blacksmith Boris", "Need a sturdy blade? Visit the shop or complete side quests to earn more gold."),
    "Merchant Lyra": NPC("Merchant Lyra", "I sell the finest health potions and equipment this side of the realm!"),
    "Hermit Bob": NPC("Hermit Bob", "Psst... monsters drop rare loot if you defeat enough of them in the forest depths."),
    "Gatekeeper Vance": NPC("Gatekeeper Vance", "Only those proven in battle may pass through to the Dragon's Lair. Prove your worth!")
}
