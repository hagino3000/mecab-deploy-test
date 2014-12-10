# coding=utf-8

import MeCab

def get_tagger():
    return MeCab.Tagger()


def extract_words(text):
    results = []
    for m in get_tagger().parse(text.encode('utf-8')).split('\n'):
        if m == 'EOS' or '':
            break
        node = m.split('\t')
        word = node[0]
        word_classes = node[1]

        if word_classes.split(',')[0] == '名詞':
            results.append(word)

    return results


def test():
    text = u'すもももももももものうち'
    result = extract_words(text)
    print(result[0])
    print(result[1])


if __name__ == '__main__':
    test()
