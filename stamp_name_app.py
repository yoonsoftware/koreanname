import streamlit as st
import re

# --- 영어→한글 발음 변환 매핑 ---
def english_to_korean(english_name):
    """영어 이름을 한글 발음으로 변환"""
    # 기본 음절 매핑 (영어 발음 → 한글)
    mapping = {
        # 남성 이름 (A-Z)
        'aaron': '아론', 'abraham': '에이브러햄', 'adam': '아담', 'adrian': '에이드리언',
        'aiden': '에이든', 'alan': '앨런', 'albert': '앨버트', 'alejandro': '알레한드로',
        'alex': '알렉스', 'alexander': '알렉산더', 'alfred': '알프레드', 'andrew': '앤드류',
        'andy': '앤디', 'angel': '안젤', 'anthony': '앤서니', 'antonio': '안토니오',
        'archie': '아치', 'arnold': '아놀드', 'arthur': '아서', 'ashton': '애슈턴',
        'austin': '오스틴', 'axel': '액셀', 'barry': '배리', 'ben': '벤',
        'benjamin': '벤자민', 'bennett': '베넷', 'blake': '블레이크', 'bobby': '바비',
        'bradley': '브래들리', 'brandon': '브랜든', 'brayden': '브레이든', 'brendan': '브렌던',
        'brent': '브렌트', 'brett': '브렛', 'brian': '브라이언', 'bruce': '브루스',
        'bryan': '브라이언', 'bryce': '브라이스', 'byron': '바이런', 'caleb': '칼렙',
        'calvin': '캘빈', 'cameron': '카메론', 'carl': '칼', 'carlos': '카를로스',
        'carter': '카터', 'casey': '케이시', 'chad': '채드', 'chandler': '챈들러',
        'charles': '찰스', 'chase': '체이스', 'chris': '크리스', 'christian': '크리스천',
        'christopher': '크리스토퍼', 'clarence': '클래런스', 'clark': '클라크', 'clayton': '클레이튼',
        'clifford': '클리포드', 'clint': '클린트', 'clinton': '클린턴', 'cody': '코디',
        'cole': '콜', 'colin': '콜린', 'connor': '코너', 'cooper': '쿠퍼',
        'corey': '코리', 'cory': '코리', 'craig': '크레이그', 'curtis': '커티스',
        'dale': '데일', 'dalton': '달튼', 'damian': '데미안', 'damon': '데이먼',
        'dan': '댄', 'daniel': '다니엘', 'danny': '대니', 'darrell': '대럴',
        'darren': '대런', 'darwin': '다윈', 'dave': '데이브', 'david': '데이비드',
        'dean': '딘', 'dennis': '데니스', 'derek': '데릭', 'derrick': '데릭',
        'devin': '데빈', 'diego': '디에고', 'dominic': '도미닉', 'don': '돈',
        'donald': '도널드', 'donnie': '도니', 'douglas': '더글러스', 'drew': '드류',
        'dustin': '더스틴', 'dwayne': '드웨인', 'dwight': '드와이트', 'dylan': '딜런',
        'earl': '얼', 'edgar': '에드가', 'edmund': '에드먼드', 'edward': '에드워드',
        'edwin': '에드윈', 'eli': '일라이', 'elijah': '일라이저', 'elliot': '엘리엇',
        'elliott': '엘리엇', 'elmer': '엘머', 'emanuel': '이매뉴얼', 'emilio': '에밀리오',
        'eric': '에릭', 'erik': '에릭', 'ernest': '어니스트', 'ethan': '이든',
        'eugene': '유진', 'evan': '에반', 'everett': '에버렛', 'ezra': '에즈라',
        'felix': '펠릭스', 'fernando': '페르난도', 'finn': '핀', 'floyd': '플로이드',
        'forrest': '포레스트', 'francis': '프랜시스', 'francisco': '프란시스코', 'frank': '프랭크',
        'franklin': '프랭클린', 'fred': '프레드', 'frederick': '프레드릭', 'gabriel': '가브리엘',
        'garrett': '개럿', 'gary': '게리', 'gavin': '개빈', 'gene': '진',
        'geoffrey': '제프리', 'george': '조지', 'gerald': '제럴드', 'gilbert': '길버트',
        'glen': '글렌', 'glenn': '글렌', 'gordon': '고든', 'grace': '그레이스',
        'graham': '그레이엄', 'grant': '그랜트', 'gregory': '그레고리', 'griffin': '그리핀',
        'guy': '가이', 'harold': '해럴드', 'harrison': '해리슨', 'harry': '해리',
        'harvey': '하비', 'hayden': '헤이든', 'hector': '헥터', 'henry': '헨리',
        'herbert': '허버트', 'herman': '허먼', 'homer': '호머', 'howard': '하워드',
        'hugh': '휴', 'hunter': '헌터', 'ian': '이안', 'ibrahim': '이브라힘',
        'isaac': '아이작', 'isaiah': '아이제이아', 'ivan': '이반', 'jack': '잭',
        'jackson': '잭슨', 'jacob': '제이콥', 'jaden': '제이든', 'jaime': '하이메',
        'jake': '제이크', 'james': '제임스', 'jamie': '제이미', 'jared': '자레드',
        'jarvis': '자비스', 'jason': '제이슨', 'jasper': '재스퍼', 'javier': '하비에르',
        'jay': '제이', 'jayden': '제이든', 'jeff': '제프', 'jefferson': '제퍼슨',
        'jeffrey': '제프리', 'jeremy': '제레미', 'jeremiah': '예레미야', 'jerome': '제롬',
        'jerry': '제리', 'jesse': '제시', 'jesus': '예수스', 'jim': '짐',
        'jimmy': '지미', 'joe': '조', 'joel': '조엘', 'joey': '조이',
        'john': '존', 'johnathan': '조나단', 'johnny': '조니', 'jonah': '조나',
        'jonathan': '조나단', 'jordan': '조던', 'jorge': '호르헤', 'jose': '호세',
        'joseph': '조지프', 'josh': '조쉬', 'joshua': '조슈아', 'juan': '후안',
        'julian': '줄리안', 'julio': '훌리오', 'justin': '저스틴', 'kai': '카이',
        'karl': '칼', 'keith': '키스', 'kelvin': '켈빈', 'ken': '켄',
        'kendall': '켄달', 'kenneth': '케네스', 'kenny': '케니', 'kevin': '케빈',
        'kieran': '키런', 'kirk': '커크', 'knox': '녹스', 'kurt': '커트',
        'kyle': '카일', 'lance': '랜스', 'landon': '랜든', 'larry': '래리',
        'lawrence': '로렌스', 'lee': '리', 'leo': '레오', 'leon': '레온',
        'leonard': '레너드', 'leonardo': '레오나르도', 'leroy': '리로이', 'leslie': '레슬리',
        'lester': '레스터', 'levi': '리바이', 'lewis': '루이스', 'liam': '리암',
        'lincoln': '링컨', 'lionel': '라이오넬', 'lloyd': '로이드', 'logan': '로건',
        'lonnie': '로니', 'lorenzo': '로렌조', 'louis': '루이스', 'lucas': '루카스',
        'luis': '루이스', 'luke': '루크', 'luther': '루터', 'lyle': '라일',
        'lyndon': '린든', 'malcolm': '말콤', 'manuel': '마누엘', 'marc': '마크',
        'marco': '마르코', 'marcus': '마커스', 'mario': '마리오', 'mark': '마크',
        'marlon': '말론', 'marshall': '마셜', 'martin': '마틴', 'marvin': '마빈',
        'mason': '메이슨', 'mathew': '매튜', 'matthew': '매튜', 'maurice': '모리스',
        'max': '맥스', 'maxwell': '맥스웰', 'melvin': '멜빈', 'micah': '마이카',
        'michael': '마이클', 'miguel': '미구엘', 'mike': '마이크', 'miles': '마일스',
        'milton': '밀튼', 'mitchell': '미첼', 'mohammed': '모하메드', 'morgan': '모건',
        'morris': '모리스', 'moses': '모세스', 'muhammad': '무함마드', 'murray': '머레이',
        'nathan': '네이선', 'nathaniel': '나다니엘', 'neil': '닐', 'nelson': '넬슨',
        'nicholas': '니콜라스', 'nick': '닉', 'nicolas': '니콜라스', 'nigel': '나이젤',
        'noah': '노아', 'noel': '노엘', 'nolan': '놀란', 'norman': '노먼',
        'oliver': '올리버', 'omar': '오마르', 'orlando': '올랜도', 'oscar': '오스카',
        'otis': '오티스', 'owen': '오웬', 'parker': '파커', 'patrick': '패트릭',
        'paul': '폴', 'pedro': '페드로', 'perry': '페리', 'pete': '피트',
        'peter': '피터', 'philip': '필립', 'phillip': '필립', 'pierce': '피어스',
        'preston': '프레스턴', 'quentin': '퀸틴', 'quinn': '퀸', 'rafael': '라파엘',
        'ralph': '랄프', 'ramon': '라몬', 'randall': '랜들', 'randy': '랜디',
        'raul': '라울', 'ray': '레이', 'raymond': '레이먼드', 'reed': '리드',
        'reginald': '레지널드', 'reid': '리드', 'rene': '르네', 'rex': '렉스',
        'ricardo': '리카르도', 'richard': '리처드', 'rick': '릭', 'ricky': '리키',
        'riley': '라일리', 'rob': '롭', 'robert': '로버트', 'roberto': '로베르토',
        'robin': '로빈', 'rodney': '로드니', 'rodrigo': '로드리고', 'roger': '로저',
        'roland': '롤랜드', 'roman': '로만', 'romeo': '로미오', 'ron': '론',
        'ronald': '로널드', 'ronnie': '로니', 'ross': '로스', 'roy': '로이',
        'ruben': '루벤', 'russell': '러셀', 'ryan': '라이언', 'sam': '샘',
        'samuel': '사무엘', 'santiago': '산티아고', 'scott': '스콧', 'sean': '숀',
        'sebastian': '세바스찬', 'sergio': '세르지오', 'seth': '세스', 'shane': '셰인',
        'shawn': '숀', 'sheldon': '셸던', 'sidney': '시드니', 'simon': '사이먼',
        'spencer': '스펜서', 'stanley': '스탠리', 'stefan': '스테판', 'stephen': '스티븐',
        'steve': '스티브', 'steven': '스티븐', 'stewart': '스튜어트', 'stuart': '스튜어트',
        'sullivan': '설리번', 'sylvester': '실베스터', 'tanner': '태너', 'taylor': '테일러',
        'ted': '테드', 'terrance': '테런스', 'terrence': '테런스', 'terry': '테리',
        'theodore': '시어도어', 'thomas': '토마스', 'tim': '팀', 'timothy': '티모시',
        'tobias': '토비아스', 'todd': '토드', 'tom': '톰', 'tommy': '토미',
        'tony': '토니', 'travis': '트래비스', 'trent': '트렌트', 'trevor': '트레버',
        'trey': '트레이', 'tristan': '트리스탄', 'troy': '트로이', 'tucker': '터커',
        'tyler': '타일러', 'tyrone': '타이론', 'ulysses': '율리시스', 'uri': '우리',
        'vernon': '버논', 'victor': '빅터', 'vincent': '빈센트', 'virgil': '버질',
        'wade': '웨이드', 'walker': '워커', 'wallace': '월리스', 'walt': '월트',
        'walter': '월터', 'warren': '워런', 'wayne': '웨인', 'wendell': '웬델',
        'wesley': '웨슬리', 'wilbur': '윌버', 'willard': '윌라드', 'william': '윌리엄',
        'willie': '윌리', 'wilson': '윌슨', 'winston': '윈스턴', 'wyatt': '와이어트',
        'xavier': '자비에르', 'zachary': '재커리', 'zane': '제인', 'zeus': '제우스',
        
        # 여성 이름 (A-Z)
        'abigail': '애비게일', 'ada': '에이다', 'addison': '애디슨', 'adele': '아델',
        'adriana': '아드리아나', 'agnes': '아그네스', 'aileen': '에일린', 'aimee': '에이미',
        'alana': '알라나', 'alberta': '앨버타', 'alexandra': '알렉산드라', 'alexis': '알렉시스',
        'alice': '앨리스', 'alicia': '알리시아', 'alison': '앨리슨', 'allison': '앨리슨',
        'alma': '알마', 'alyssa': '알리사', 'amanda': '아만다', 'amber': '앰버',
        'amelia': '아멜리아', 'amy': '에이미', 'ana': '아나', 'andrea': '안드레아',
        'angel': '엔젤', 'angela': '안젤라', 'angelica': '안젤리카', 'angelina': '안젤리나',
        'anita': '아니타', 'ann': '앤', 'anna': '안나', 'annabelle': '애너벨',
        'anne': '앤', 'annette': '애넷', 'annie': '애니', 'antoinette': '앙투아네트',
        'april': '에이프릴', 'aria': '아리아', 'ariana': '아리아나', 'ariel': '아리엘',
        'arlene': '알린', 'ashley': '애슐리', 'athena': '아테나', 'aubrey': '오브리',
        'audrey': '오드리', 'aurora': '오로라', 'autumn': '오텀', 'ava': '에이바',
        'avery': '에이버리', 'barbara': '바바라', 'beatrice': '베아트리체', 'becky': '베키',
        'belinda': '벨린다', 'bella': '벨라', 'bernadette': '버나뎃', 'bernice': '버니스',
        'bertha': '버사', 'bessie': '베시', 'beth': '베스', 'bethany': '베서니',
        'betty': '베티', 'beverly': '베벌리', 'bianca': '비앙카', 'billie': '빌리',
        'blanche': '블랑슈', 'bobbie': '바비', 'bonnie': '보니', 'brandi': '브랜디',
        'brandy': '브랜디', 'brenda': '브렌다', 'brianna': '브리아나', 'bridget': '브리짓',
        'brittany': '브리트니', 'brooke': '브룩', 'brooklyn': '브루클린', 'caitlin': '케이틀린',
        'camila': '카밀라', 'camille': '카밀', 'candace': '캔디스', 'candice': '캔디스',
        'cara': '카라', 'carla': '칼라', 'carmen': '카르멘', 'carol': '캐롤',
        'carole': '캐롤', 'caroline': '캐롤라인', 'carolyn': '캐롤린', 'carrie': '캐리',
        'cassandra': '카산드라', 'cassidy': '캐시디', 'catherine': '캐서린', 'cathy': '캐시',
        'cecelia': '세실리아', 'cecilia': '세실리아', 'celeste': '셀레스트', 'celia': '셀리아',
        'charlene': '샬린', 'charlotte': '샬롯', 'charmaine': '샤메인', 'chelsea': '첼시',
        'cheryl': '셰릴', 'chloe': '클로이', 'christa': '크리스타', 'christi': '크리스티',
        'christian': '크리스챤', 'christina': '크리스티나', 'christine': '크리스틴', 'christy': '크리스티',
        'cindy': '신디', 'claire': '클레어', 'clara': '클라라', 'clare': '클레어',
        'clarissa': '클라리사', 'claudia': '클라우디아', 'cleo': '클레오', 'colleen': '콜린',
        'connie': '코니', 'constance': '콘스탄스', 'cora': '코라', 'corina': '코리나',
        'courtney': '코트니', 'crystal': '크리스털', 'cynthia': '신시아', 'daisy': '데이지',
        'dana': '데이나', 'danielle': '다니엘', 'daphne': '다프네', 'darlene': '달린',
        'dawn': '던', 'deanna': '디애나', 'debbie': '데비', 'deborah': '데보라',
        'debra': '데브라', 'delia': '델리아', 'delilah': '딜라일라', 'delores': '돌로레스',
        'denise': '데니스', 'desiree': '데지레', 'destiny': '데스티니', 'diana': '다이애나',
        'diane': '다이앤', 'dianne': '다이앤', 'dolores': '돌로레스', 'dominique': '도미니크',
        'donna': '도나', 'dora': '도라', 'doreen': '도린', 'doris': '도리스',
        'dorothy': '도로시', 'edith': '이디스', 'edna': '에드나', 'eileen': '에일린',
        'elaine': '일레인', 'eleanor': '엘리너', 'elena': '엘레나', 'elise': '엘리스',
        'eliza': '엘라이자', 'elizabeth': '엘리자베스', 'ella': '엘라', 'ellen': '엘런',
        'ellie': '엘리', 'eloise': '엘로이즈', 'elsa': '엘사', 'elsie': '엘시',
        'elvira': '엘비라', 'emily': '에밀리', 'emma': '엠마', 'erica': '에리카',
        'erin': '에린', 'erma': '어마', 'esmeralda': '에스메랄다', 'esperanza': '에스페란자',
        'estelle': '에스텔', 'esther': '에스더', 'ethel': '에델', 'etta': '에타',
        'eunice': '유니스', 'eva': '에바', 'evelyn': '에블린', 'faith': '페이스',
        'fannie': '패니', 'faye': '페이', 'felicia': '펠리시아', 'flora': '플로라',
        'florence': '플로렌스', 'frances': '프랜시스', 'francine': '프랜신', 'francisca': '프란시스카',
        'freda': '프리다', 'gabriela': '가브리엘라', 'gabriella': '가브리엘라', 'gabrielle': '가브리엘',
        'gail': '게일', 'genesis': '제네시스', 'genevieve': '제네비브', 'georgia': '조지아',
        'geraldine': '제럴딘', 'gertrude': '거트루드', 'gina': '지나', 'ginger': '진저',
        'gladys': '글래디스', 'glenda': '글렌다', 'gloria': '글로리아', 'grace': '그레이스',
        'gracie': '그레이시', 'gretchen': '그레첸', 'guadalupe': '과달루페', 'gwendolyn': '그웬돌린',
        'haley': '헤일리', 'hannah': '한나', 'harmony': '하모니', 'harriet': '해리엇',
        'hattie': '해티', 'hazel': '헤이즐', 'heather': '헤더', 'heidi': '하이디',
        'helen': '헬렌', 'helena': '헬레나', 'hilda': '힐다', 'hillary': '힐러리',
        'holly': '홀리', 'hope': '호프', 'ida': '아이다', 'imogene': '이모진',
        'ingrid': '잉그리드', 'irene': '아이린', 'iris': '아이리스', 'irma': '어마',
        'isabel': '이사벨', 'isabella': '이사벨라', 'isabelle': '이사벨', 'ivy': '아이비',
        'jackie': '재키', 'jacqueline': '재클린', 'jacquelyn': '재클린', 'jade': '제이드',
        'jamie': '제이미', 'jan': '잰', 'jana': '재나', 'jane': '제인',
        'janelle': '자넬', 'janet': '자넷', 'janice': '재니스', 'janie': '재니',
        'janine': '자닌', 'jasmine': '재스민', 'jean': '진', 'jeanette': '지넷',
        'jeanne': '진', 'jeannie': '지니', 'jennie': '제니', 'jennifer': '제니퍼',
        'jenny': '제니', 'jeri': '제리', 'jessica': '제시카', 'jessie': '제시',
        'jill': '질', 'jillian': '질리안', 'jo': '조', 'joan': '조안',
        'joann': '조앤', 'joanna': '조애나', 'joanne': '조앤', 'jocelyn': '조슬린',
        'jodi': '조디', 'jodie': '조디', 'josephine': '조세핀', 'joy': '조이',
    
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
