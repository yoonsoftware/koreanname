import streamlit as st
import re

# --- 영어→한글 발음 변환 매핑 ---
def english_to_korean(english_name):
    """영어 이름을 한글 발음으로 변환"""
    # 기본 음절 매핑 (영어 발음 → 한글)
    mapping = {
        'michael': '마이클', 'johnson': '존슨', 'smith': '스미스',
        'john': '존', 'mary': '메리', 'james': '제임스',
        'robert': '로버트', 'patricia': '패트리샤', 'jennifer': '제니퍼',
        'linda': '린다', 'william': '윌리엄', 'david': '데이비드',
        'richard': '리처드', 'susan': '수잔', 'jessica': '제시카',
        'sarah': '사라', 'karen': '카렌', 'nancy': '낸시',
        'betty': '베티', 'margaret': '마가렛', 'sandra': '산드라',
        'ashley': '애슐리', 'dorothy': '도로시', 'kimberly': '킴벌리',
        'emily': '에밀리', 'donna': '도나', 'michelle': '미셸',
        'carol': '캐롤', 'amanda': '아만다', 'melissa': '멜리사',
        'deborah': '데보라', 'stephanie': '스테파니', 'rebecca': '레베카',
        'laura': '로라', 'sharon': '샤론', 'cynthia': '신시아',
        'kathleen': '캐슬린', 'amy': '에이미', 'shirley': '셜리',
        'angela': '안젤라', 'helen': '헬렌', 'anna': '안나',
        'brenda': '브렌다', 'pamela': '파멜라', 'nicole': '니콜',
        'samantha': '사만다', 'katherine': '캐서린', 'emma': '엠마',
        'ruth': '루스', 'christine': '크리스틴', 'catherine': '캐서린',
        'debra': '데브라', 'rachel': '레이첼', 'carolyn': '캐롤린',
        'janet': '자넷', 'virginia': '버지니아', 'maria': '마리아',
        'thomas': '토마스', 'charles': '찰스', 'christopher': '크리스토퍼',
        'daniel': '다니엘', 'matthew': '매튜', 'anthony': '앤서니',
        'donald': '도널드', 'mark': '마크', 'paul': '폴',
        'steven': '스티븐', 'andrew': '앤드류', 'kenneth': '케네스',
        'joshua': '조슈아', 'kevin': '케빈', 'brian': '브라이언',
        'george': '조지', 'edward': '에드워드', 'ronald': '로널드',
        'timothy': '티모시', 'jason': '제이슨', 'jeffrey': '제프리',
        'ryan': '라이언', 'jacob': '제이콥', 'gary': '게리',
        'nicholas': '니콜라스', 'eric': '에릭', 'stephen': '스티븐',
        'jonathan': '조나단', 'larry': '래리', 'justin': '저스틴',
        'scott': '스콧', 'brandon': '브랜든', 'frank': '프랭크',
        'benjamin': '벤자민', 'gregory': '그레고리', 'raymond': '레이몬드',
        'samuel': '사무엘', 'patrick': '패트릭', 'alexander': '알렉산더',
        'jack': '잭', 'dennis': '데니스', 'jerry': '제리',
        'tyler': '타일러', 'aaron': '아론', 'jose': '호세',
        'henry': '헨리', 'douglas': '더글러스', 'adam': '아담',
        'peter': '피터', 'nathan': '네이선', 'zachary': '재커리',
        'walter': '월터', 'kyle': '카일', 'harold': '해럴드',
        'carl': '칼', 'jeremy': '제레미', 'keith': '키스',
        'roger': '로저', 'gerald': '제럴드', 'ethan': '이단',
    }
    
    name_lower = english_name.strip().lower()
    name_lower = re.sub(r'[^a-z\s]', '', name_lower)
    parts = name_lower.split()
    
    korean_parts = []
    for part in parts:
        if part in mapping:
            korean_parts.append(mapping[part])
        else:
            # 매핑에 없는 경우 음절별 변환 시도
            korean_parts.append(phonetic_convert(part))
    
    return ' '.join(korean_parts)

def phonetic_convert(text):
    """간단한 음절 단위 발음 변환"""
    consonants = {
        'b': 'ㅂ', 'c': 'ㅋ', 'd': 'ㄷ', 'f': 'ㅍ', 'g': 'ㄱ',
        'h': 'ㅎ', 'j': 'ㅈ', 'k': 'ㅋ', 'l': 'ㄹ', 'm': 'ㅁ',
        'n': 'ㄴ', 'p': 'ㅍ', 'q': 'ㅋ', 'r': 'ㄹ', 's': 'ㅅ',
        't': 'ㅌ', 'v': 'ㅂ', 'w': 'ㅜ', 'x': 'ㅋㅅ', 'y': 'ㅣ', 'z': 'ㅈ'
    }
    vowels = {
        'a': '아', 'e': '에', 'i': '이', 'o': '오', 'u': '우',
        'ea': '이', 'ee': '이', 'oo': '우', 'ou': '아우'
    }
    
    # 간단한 변환 (실제로는 더 복잡한 규칙 필요)
    result = ''
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i:i+2] in vowels:
            result += vowels[text[i:i+2]]
            i += 2
        elif text[i] in vowels:
            result += vowels[text[i]]
            i += 1
        elif text[i] in consonants:
            result += consonants[text[i]]
            i += 1
        else:
            i += 1
    
    return result if result else text

def make_stamp_name(english_name):
    """도장 이름 생성"""
    korean_name = english_to_korean(english_name)
    
    # 공백 제거하고 도장 이름 생성
    korean_clean = korean_name.replace(' ', '')
    
    # 도장에 적합한 길이로 축약 (최대 4글자)
    max_len = 4
    if len(korean_clean) > max_len:
        # 첫 2글자 + 마지막 1글자
        short_name = korean_clean[:2] + korean_clean[-1]
    else:
        short_name = korean_clean
    
    return korean_name, short_name

# --- Streamlit UI ---
st.set_page_config(page_title="K-Stamp Generator", page_icon="🪶", layout="centered")

st.title("🪶 K-Stamp Name Creator")
st.subheader("Transform your name into a beautiful Korean seal name!")
st.write("Example: Michael Johnson → 마이클 존슨 → **마슨**")

english_name = st.text_input("✍️ Enter your English name", placeholder="Example: Michael Johnson")

if english_name:
    korean_name, short_name = make_stamp_name(english_name)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Input Name", english_name)
    with col2:
        st.metric("Korean Pronunciation", korean_name)
    with col3:
        st.metric("Seal Name", f"🪶 {short_name}")
        # 클릭하면 복사되는 버튼
        if st.button("📋 Copy seal name", key="copy_btn", use_container_width=True):
            st.code(short_name, language=None)
    st.markdown("---")
    st.info("💡 A short and simple name fits better with the seal design.")
    
    # 추가 정보
    with st.expander("📝 Conversion Guide"):
        st.write("""
        - The Korean conversion program is not perfect. If an incorrect conversion occurs, the seal will be engraved based on the original name.
        - Common English names are automatically converted to Korean pronunciation.
        - The seal name is shortened to 2–4 characters.
        - Special characters and numbers are automatically removed.
        - Names not found in the mapping are converted by syllable.
        """)

st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; margin-top:40px; color:gray; font-size:14px'>
    © 2025 K-Stamp Project | Feel the Beauty of Hangul
    </div>
    """,
    unsafe_allow_html=True
)
