from string import Template 

subs = dict(who ="you" ,whom ="me")

file=Template("$who  owe the money to $whom").substitute(subs)

print(file)
