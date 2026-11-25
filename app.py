import streamlit as st

# 혈액형별 가질 수 있는 대립유전자 딕셔너리
genes = {
    'A': ['A', 'O'],
    'B': ['B', 'O'],
    'AB': ['A', 'B'],
    'O': ['O', 'O'],
}


# 두 유전자(g1, g2)를 합쳐 자녀의 혈액형을 판단하는 함수
def get_child(g1, g2):
    pair = g1 + g2
    if 'A' in pair and 'B' in pair:
        return 'AB'
    elif 'A' in pair:
        return 'A'
    elif 'B' in pair:
        return 'B'
    else:
        return 'O'


# --- Streamlit 웹앱 화면 구성 ---
st.set_page_config(page_title='2세 혈액형 예측기', page_icon='🩸')

st.title('🩸 부모 혈액형으로 알아보는 2세 혈액형')
st.write('아버지와 어머니의 혈액형을 선택하고 버튼을 눌러보세요!')
st.divider()

col1, col2 = st.columns(2)
blood_types = ['A', 'B', 'AB', 'O']

with col1:
    father = st.selectbox('👨 아버지의 혈액형', blood_types)

with col2:
    mother = st.selectbox('👩 어머니의 혈액형', blood_types)

st.write('')

if st.button('2세 혈액형 확인하기', type='primary', use_container_width=True):
    # 중복 없이 가능한 혈액형을 담을 집합(set)
    possible_bloods = set()

    # 이중 for문을 사용해 부모의 모든 유전자 조합 확인
    for g1 in genes[father]:
        for g2 in genes[mother]:
            child_bt = get_child(g1, g2)
            possible_bloods.add(child_bt)

    # 결과를 보기 좋게 정렬 후 문자열로 나열
    result_list = sorted(list(possible_bloods))
    result_text = ', '.join([bt + '형' for bt in result_list])

    st.success(
        f'**{father}형** 아버지와 **{mother}형** 어머니 사이에서 나올 수 있는'
        ' 혈액형은 다음과 같습니다!'
    )
    st.subheader(f'👉 {result_text}')
