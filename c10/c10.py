#!/usr/bin/env python3

# # When clicking on the cow we get the following text: `a = [1, 11, 21, 1211, 111221,`
# # Thinking about this you see that this looks kinda like a run-length encoding, so 
# # we built one for the sake of the challenge...

seq="1"
for i in range(30):
    st = ""
    while len(seq)>0:
        m = re.search( r'^([0-9])\1*', seq).group()
        seq = seq[len(m):]
        st += f"{len(m)}{m[0]}"
    seq=st
len(st)