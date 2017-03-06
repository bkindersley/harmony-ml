print('starting script')
from music21 import *
print('done import')

def processScore(s):
    #extract soprano (melody) and alto (harmony) parts
    #recurse method works to recursively search through
    #different streams
    p0 = s.parts[0].recurse().getElementsByClass(note.Note).stream()
    p1 = s.parts[1].recurse().getElementsByClass(note.Note).stream()

    #new score from extracted parts
    s2 = stream.Stream()
    s2.insert(p0)
    s2.insert(p1)

    #turn into chords
    c = s2.chordify().getElementsByClass(chord.Chord)

    #counter
    i = 0
    #input vector
    x = []
    #target vector
    t = []
    f = open('harmonyData.csv', 'a')
    #for each chord
    for ch in c.notes:
        #every 8 notes
        if (i%8 == 0):
            #if have a complete phrase
            if (len(x) == 8):
                #print(','.join(x) + ',' + ','.join(t)+'\n')
                f.write(','.join(x) + ',' + ','.join(t)+'\n')
            #clear vectors
            x = []
            t = []
        i = i+1
        #if have a chord (no rest)
        if (len(ch) == 2):
            x.append("{0}".format(ch.pitches[0].midi))
            t.append("{0}".format(ch.pitches[1].midi))
    f.close()

i = 0
f = open('harmonyData.csv', 'w')
f.write('x0,x1,x2,x3,x4,x5,x6,x7,t0,t1,t2,t3,t4,t5,t6,t7\n')
f.close()
for work in corpus.chorales.Iterator():
    i = i+1
    print('new work {0}'.format(i))
    processScore(work)
