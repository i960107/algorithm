# # import spacy
#
# nlp = spacy.load("en_core_web_sm")
#
#
# def anonymize_text(sentences: str) -> str:
#     answer = []
#     doc = nlp(sentences)
#
#
#     for ent in doc.ents:
#         if ent.label == "PERSON":
#             answer.append("person")
#         elif ent.label == "NAME":
#             answer.append("name")
#
#     answer = [x for x in sentences]
#
#     return ''.join(answer)
#
#
# print(anonymize_text("John in old"))
# print(anonymize_text("Mark Oldham ate an apple"))
s1, e1 = 0, 4
s2, e2 = 19, 23
s =  set()
s.update(list(range(s1, e1)))
s.update(list(range(s2, e2)))

print(s)

indices = set()

doc = nlp(sentences)

for ent in doc.ents:
    indices.update(range(ent.start_char, ent.end_char))

return [x if i not in indices else "X" for i, x in enumerate(sentences)]