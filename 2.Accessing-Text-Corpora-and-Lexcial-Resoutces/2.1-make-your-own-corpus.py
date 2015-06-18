from nltk.corpus import BracketParseCorpusReader;
corpus_root = r"xenopedia";
file_pattern = r".*\.txt";

ptb = BracketParseCorpusReader(corpus_root,file_pattern);

print ptb.fileids();
print len(ptb.sents());
print ptb.sents();
