!pip install checklist &> /dev/null

import checklist
import pprint as pp

from checklist.editor import Editor
editor = Editor() # a data editor for creating/editing test examples

adj_a = ['colorless', 'odorless', 'frisky', 'frail', 'sly', 'flightless', 'winged', 'feathered', 'seaworthy', 'faint', 'bony', 'glowing', 'smudged', 'puffy', 'fermented']
adj_b = ['green', 'yellow', 'white', 'blue', 'solid', 'smelly', 'light', 'fluffy', 'silver', 'transparent', 'dim', 'oily', 'pink', 'nervous', 'skinny', 'fat']
thing = ['ideas', 'thoughts', 'plans', 'drafts', 'goals', 'dreams', 'hopes','desires','sketches','puzzles', 'wishes', 'opinions', 'facts', 'tenets', 'arguments', 'agreements', 'compliments', 'debates', 'discussions', 'awards', 'realities', 'scenarios', 'stories']
verb = ['sleep', 'nap', 'twirl', 'swim', 'drizzle', 'sag', 'spill', 'slide', 'splash', 'punch', 'spin', 'display', 'smile', 'wail', 'leap']
adverb = ['furiously', 'avidly', 'merrily', 'fervently', 'sparingly', 'blandly', 'confidently', 'plainly', 'lovingly', 'foolishly', 'dryly', 'by chance', 'chaotically', 'awkwardly', 'secretly']
combo_temp = editor.template('The {adj_a} {adj_b} {thing} {verb} {thing2} {adverb}.',
                            adj_a=adj_a, adj_b=adj_b, thing=thing, verb=verb,
                            adverb=adverb, labels=0, save=True, nsamples=100)
print("Combinations to use in replacement:")
pp.pprint(combo_temp["data"])

#inspired by code from lab 9 with Angelica
