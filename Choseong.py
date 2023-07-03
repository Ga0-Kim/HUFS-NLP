# 초성이 되는 자음 목록
choseong_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성이 되는 모음 목록
joongseong_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성의 경우 자음도 되고, 이중자음도 가능하며 없을 수도 있음.(공백)
jongseong_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def decompose(word1, word2):
    # 분리한 자모를 저장할 빈 배열
    word_list1 = []
    for letter in list(word1.strip()): # 공백 제거 필요
        if '가' <= letter <= '힣':
            # 588개마다 초성이 바뀜.
            char1 = (ord(letter) - ord('가')) // 588
            # 중성은 28가지 종류
            char2 = ((ord(letter) - ord('가')) - (588 * char1)) // 28
            char3 = ((ord(letter) - ord('가')) - (588 * char1)) - 28 * char2
            # 분리한 자모를 word_list에 추가
            # 초성, 중성, 종성을 각각 저장
            word_list1.append([choseong_list[char1], joongseong_list[char2], jongseong_list[char3]])
        else:
            word_list1.append([letter])
    word_list2 = []
    for letter in list(word2.strip()): # 공백 제거 필요
        if '가' <= letter <= '힣':
            # 588개마다 초성이 바뀜.
            char1 = (ord(letter) - ord('가')) // 588
            # 중성은 28가지 종류
            char2 = ((ord(letter) - ord('가')) - (588 * char1)) // 28
            char3 = ((ord(letter) - ord('가')) - (588 * char1)) - 28 * char2
            # 분리한 자모를 word_list에 추가
            # 초성, 중성, 종성을 각각 저장
            word_list2.append([choseong_list[char1], joongseong_list[char2], jongseong_list[char3]])
        else:
            word_list2.append([letter])
    print(word_list1, word_list2)

str1 = input('자모를 해체할 문자열을 입력하세요: ')
str2 = input('자모를 해체할 문자열을 입력하세요: ')

decompose(str1, str2)