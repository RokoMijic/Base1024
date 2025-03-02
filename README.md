# Base1024
A number system that uses unicode characters to encode 10 bits per character, using 0k as the prefix to differentiate itself from hexadecimals.

Some examples:


	
	0k₶℀⬱♖Ⓓ⋐⊪⊺⍍⎶⩍⌮⨐①⚃ᚪ
	0k₶℀❑⋕⍚⩭⨻⚻⪭∑✬⨚∏⪮⪪⬨
	0kℝⰽ∞⚶ⰿⓊↁ℗⧌⪗⟒†⩧∯⫝⨤
	0k‽⨝⊰ℎηε⍗₯◅⑨⫤⓪⊎⨄⏂ᛟ
	0k⁒ⓩ♲④☍⍧⍓⩫⎀⫨⦹‽⏅ℓ⎈✽
	0k‡ⱑⰚ⊬⍏Ⓘ⟥℟⋭⟚≨⑭⊺Ⰰⱉ⨢


The pool of characters is currently 1202 and not finalized - more analysis is required to cut unsuitable characters from the pool, or potentially add new ones. It is not recommended to use this project right now. 

Initial pool of 1202 unicode characters in the 0000-FFFF range chosen for 

- wide compatibility
- no emojis
- no characters that are too dark 
- no characters that are too wide or too narrow, too short or too tall
- no common modern languages except greek

Base4096 is a possible extention of this project, likely with a nonoverlapping set.
