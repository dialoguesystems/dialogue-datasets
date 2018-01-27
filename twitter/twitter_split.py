import numpy as np
lines = open("twitter.dlg.cleaned.txt", "r").readlines()

train_context_writer = open("twitter_train_context.txt", "w")
train_response_writer = open("twitter_train_response.txt", "w")
valid_context_writer = open("twitter_valid_context.txt", "w")
valid_response_writer = open("twitter_valid_response.txt", "w")
test_context_writer = open("twitter_test_context.txt", "w")
test_response_writer = open("twitter_test_response.txt", "w")

contexts = []
responses = []
for line in lines:
    utterances = [utterance for utterance in line.strip().split("  __eou__  ") if len(utterance) > 0]
    if len(utterances) > 1:
        contexts.append("  __eou__   ".join(utterances[-6:-1]))
        responses.append(utterances[-1])

indexes = np.arange(len(contexts))
assert len(contexts) == len(responses), "not equal."
np.random.shuffle(indexes)

for i in range(350000):
    train_context_writer.write(contexts[indexes[i]] + "\n")
    train_response_writer.write(responses[indexes[i]] + "\n")

for i in range(350000, 361600):
    valid_context_writer.write(contexts[indexes[i]] + "\n")
    valid_response_writer.write(responses[indexes[i]] + "\n")

for i in range(361600, 371601):
    test_context_writer.write(contexts[indexes[i]] + "\n")
    test_response_writer.write(responses[indexes[i]] + "\n")