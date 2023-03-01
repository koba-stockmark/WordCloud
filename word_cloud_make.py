from wordcloud import WordCloud
import re
import glob

stop_words = ["これ", "それ", "どれ", "あれ", "今", "私", "日本", "世界", "企業", "目", "人", "が", "を", "に", "の",
			  "技術","手法","開発",
			  "取扱", "新製品", "初", "方",
			  "1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月",
			  "1つ", "2つ", "3つ", "4つ", "5つ", "6つ", "7つ", "8つ", "9つ", "何",
			  "ディープテック"
			  ]

test_files = [
	"test.txt"
]

files = glob.glob("*.txt")
for file_name in files:
	print(file_name)
	text = ""
	words = []
	pre_word = ""
	with open(file_name) as f:
		for s_line in f:
			in_word =  s_line.replace("\n", "")
			if in_word == pre_word:
				continue
			pre_word = in_word
			while in_word and  in_word[0] == "。":
				in_word = in_word[1:]
			while in_word and in_word[-1] == "。":
				in_word = in_word[:-1]
			if not in_word:
				continue
			in_word = in_word.replace(" ", "_")
			in_word = in_word.replace("!", "_")
			in_word = in_word.replace("。", "_")
#			in_word = in_word.replace("「", "_")
#			in_word = in_word.replace("」", "_")
			in_word = in_word.replace("「", "")
			in_word = in_word.replace("」", "")
			in_word = in_word.replace("（", "")
			in_word = in_word.replace("）", "")
			if not in_word:
				continue
			while in_word[-1] == "_":
				in_word = in_word[:-1]
			if re.match(".*年.*月", in_word):
				continue
			words.append(in_word)

	text = ' '.join(words)


	#ワードクラウドを作成
	wordcloud = WordCloud(
		width = 2000,  # 幅
		height = 1500,  # 高さ
		background_color = 'white', # 背景色
#		collocations = False,
		font_path = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf', # 日本語フォントを指定
		stopwords = set(stop_words), # 出力から除外する単語
	)

	wordcloud.generate(text)
	wordcloud.to_file(file_name.split(".")[0] + ".png")