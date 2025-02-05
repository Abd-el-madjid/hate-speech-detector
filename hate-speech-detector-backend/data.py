import pandas as pd

# Extended list of hate words
hate_words = [
    "abandonment", "abortion", "abuse", "adversary", "affront", "aggressor", "alienate", "anger", "animosity", "antagonism",
    "antagonist", "assault", "atrocity", "awful", "bastard", "bigot", "bitch", "blasphemy", "blow", "bullshit", "cancer", "cocksucker",
    "condemnation", "coward", "cruel", "criminal", "cuck", "cunt", "damn", "dangerous", "death", "defamation", "dehumanize", "demonize",
    "denigration", "destruction", "devil", "disgusting", "disgrace", "disrespect", "dog", "douche", "dyke", "enemy", "evil", "exclusion",
    "failure", "faggot", "fake", "fool", "fraud", "freak", "fuck", "garbage", "genocide", "grief", "hate", "hell", "hostility", "hypocrite",
    "ignorant", "inferior", "insult", "irresponsible", "irritating", "jealous", "kill", "liar", "loser", "lunatic", "malice", "manipulate",
    "murder", "nazi", "offensive", "oppressor", "parasite", "pathetic", "perversion", "piss", "prejudice", "psychopath", "racist", "rapist",
    "rejection", "retard", "scum", "selfish", "sexist", "shit", "slut", "stupid", "suck", "terrorist", "thug", "troll", "useless", "victim",
    "violence", "vulgar", "wimp", "worthless", "asshole", "bastard", "beast", "bitch", "blackmail", "blowjob", "bully", "cancer", "cheat",
    "cheater", "cock", "contempt", "criminal", "cuckold", "cunt", "curse", "demon", "discrimination", "doormat", "douchebag", "dyke", "emotional",
    "embarrassment", "envious", "evil", "exile", "foolish", "freak", "fuckwit", "garbage", "guilty", "hateful", "hellbound", "ignorant",
    "inconsiderate", "inferior", "insensitive", "insulting", "irritable", "jealousy", "killer", "lackey", "leech", "loser", "manipulative",
    "masochist", "murderer", "nazi", "neglect", "offender", "oppressor", "pathetic", "pedophile", "pervert", "pussy", "rejection", "resentment",
    "scoundrel", "sexist", "sick", "slime", "sociopath", "threat", "toxic", "traitor", "vicious", "vulgar", "waste", "weakling", "whore", "wimp",
    "zombie", "abhor", "abhorrent", "abusive", "alienating", "annoyance", "apathy", "arrogant", "asshole", "atrocious", "barbaric", "beating",
    "betrayal", "bitch", "blacklist", "blasphemous", "bullying", "cheater", "cocksucker", "cowardice", "creep", "cruelty", "cuntish", "damned",
    "degraded", "delusional", "demonic", "desecration", "disdain", "disrespectful", "dominating", "douche", "dreadful", "drunk", "evil-minded",
    "exclusionary", "fascist", "filth", "foolishness", "fuckhead", "garbage", "hatred", "hellish", "ignorance", "imbecile", "inadequate", "insulting",
    "intolerance", "jealousy", "judgmental", "killer", "knave", "lame", "manipulative", "murderous", "narcissist", "negativity", "nonentity",
    "odious", "oppressor", "overbearing", "pariah", "pathetic", "pedophile", "pervert", "pussy", "rejection", "resentful", "retardation",
    "revile", "scoundrel", "shameful", "sickening", "sinister", "spiteful", "stupid", "subhuman", "swine", "terrorist", "toxic", "unwanted", "vile",
    "villainous", "vindictive", "violent", "weak", "worthless", "xenophobic", "yuck"
]

# Convert the list to a DataFrame
df = pd.DataFrame(hate_words, columns=["hate_word"])

# Save the DataFrame to a CSV file
df.to_csv('hate_words_extended.csv', index=False)

print("Extended hate words CSV created successfully!")
