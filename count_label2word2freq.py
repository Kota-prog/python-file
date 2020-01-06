import sys

from fractions import Fraction

import MeCab

path_output_p_label = 'output_p_label.txt'

path_output_p_label2word = 'output_p_label2word.txt'

mecab = MeCab.Tagger("-Owakati")


def reading_file(input_file_name):
    mails = []

    with open(input_file_name, 'r', encoding="utf-8_sig")as f:
        for mail in f:
            mails.append(mail)

    return mails


def split_mails_into_labels_and_sentences(mails):
    labels = []
    sentences = []

    for mail in mails:
        label, sentence = mail.split(',')

        sentence = sentence.rstrip()

        labels.append(label)

        sentences.append(sentence)

    return labels, sentences


def count_label2freq(labels):
    label2freq = {}

    for label in labels:
        label2freq[label] = label2freq.get(label, 0) + 1

    return label2freq


def count_total_labels(label2freq):
    total_labels = 0
    for value in label2freq.values():
        total_labels += value

    return total_labels


def count_labels_probability(label2freq, total_labels):
    p_label = {}
    for key, value in label2freq.items():
        p_label[key] = Fraction(value, total_labels)

    return p_label


def output_p_label(p_label):
    with open(path_output_p_label, mode='w', encoding="utf-8_sig") as f:
        for key, value in p_label.items():
            print(f'P{key} = {value}', file=f)


def count_label2word2freq(labels, sentences):
    label2word2freq = {}

    for (label, sentence) in zip(labels, sentences):
        label2word2freq[label] = label2word2freq.get(label, {})

        words = mecab.parse(sentence).split(' ')

        for word in words:
            label2word2freq[label][word] = label2word2freq[label].get(word, 0) + 1

    return label2word2freq


def count_total_label2word(label2word2freq):
    total_label2word2freq = {}

    for label in label2word2freq.keys():
        for freq in label2word2freq[label].values():
            total_label2word2freq[label] = total_label2word2freq.get(label, 0) + int(freq)

    return total_label2word2freq


def count_label2word_probability(label2word2freq, total_label2word2freq):
    p_label2word = {}

    for label in label2word2freq.keys():
        p_label2word[label] = p_label2word.get(label, {})

        for word, freq in label2word2freq[label].items():
            p_label2word[label][word] = Fraction(freq, total_label2word2freq[label])

    return p_label2word


def output_p_label2word(p_label2word):
    with open(path_output_p_label2word, mode='w', encoding="utf-8_sig") as f:
        for label in p_label2word.keys():
            for word, probability in p_label2word[label].items():
                print(f'P{label} {word} {probability}', file=f)


def main():
    input_file_name = sys.argv[1]

    mails = reading_file(input_file_name)

    labels, sentences = split_mails_into_labels_and_sentences(mails)

    label2freq = count_label2freq(labels)

    total_labels = count_total_labels(label2freq)

    p_label = count_labels_probability(label2freq, total_labels)

    output_p_label(p_label)

    label2word2freq = count_label2word2freq(labels, sentences)

    total_label2word2freq = count_total_label2word(label2word2freq)

    p_label2word = count_label2word_probability(label2word2freq, total_label2word2freq)

    output_p_label2word(p_label2word)


if __name__ == '__main__':
    main()
