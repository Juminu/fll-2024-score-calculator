import streamlit as st
from streamlit_float import *

ss =st.session_state

if 'score' not in ss:
    ss.score = 0
    # ss.장비점검 = 0
    # ss.삼디영화관 = 0 
    # ss.극장장면전환 = 0
    # ss.몰입한경험 = 0
    # ss.마스터피스 = 0
    # ss.마스터피스2 = 0
    # ss.증강현실동상 = 0
    # ss.음악콘서트조명과소리 = 0
    # ss.음악콘서트조명과소리1 = 0
    # ss.홀로그램연기자 = 0
    # ss.영화세트장 = 0
    # ss.사운드믹서 = 0
    # ss.라이트쇼 = 0
    # ss.가상현실아티스트 = 0
    # ss.공예품창작자 = 0
    # ss.관객이동 = 0
    # ss.전문가이동 = 0
    # ss.정밀토큰 = 0
    ss.장비점검점수 = 0
    ss.삼디영화관점수 = 0 
    ss.극장장면전환점수 = 0
    ss.몰입한경험점수 = 0
    ss.마스터피스점수 = 0
    ss.마스터피스2점수 = 0
    ss.증강현실동상점수 = 0
    ss.음악콘서트조명과소리점수 = 0
    ss.음악콘서트조명과소리1점수 = 0
    ss.홀로그램연기자점수 = 0
    ss.영화세트장점수 = 0
    ss.영화세트장1점수 = 0
    ss.사운드믹서점수 = 0
    ss.라이트쇼점수 = 0
    ss.가상현실아티스트점수 = 0 
    ss.가상현실아티스트1점수 = 0
    ss.공예품창작자점수 = 0
    ss.공예품창작자1점수 = 0
    ss.관객이동점수 = 0
    ss.전문가이동점수 = 0
    ss.정밀토큰점수 = 0

    
def cal_score():
    # 점수2
    # ss.장비점검점수 = 20 if ss.장비점검 == True else 0
    # ss.장비점검점수 = 20 if ss.장비점검 else 0
    
    if ss.장비점검 == True:
        ss.장비점검점수 = 20
        print("장비점검 점수업")
    elif ss.장비점검 == False:
        ss.장비점검점수 = 0
        print("장비점검 점수업")

    if ss.삼디영화관 == True:
        ss.삼디영화관점수 = 20
        print("삼디영화관 점수업")
    elif ss.삼디영화관 == False:
        ss.삼디영화관점수 = 0
        print("삼디영화관 점수업")

    if ss.극장장면전환 == '체크안됨(0점)':
        ss.극장장면전환점수 = 0
    elif ss.극장장면전환 == '파란색(10점)':
        ss.극장장면전환점수 = 10
    elif ss.극장장면전환 == '분홍색(20점)':
        ss.극장장면전환점수 = 20
    else:
        ss.극장장면전환점수 = 30

    # 점수2
    if ss.몰입한경험 == True:
        ss.몰입한경험점수 = 20
        print("몰입한경험 점수업")
    elif ss.몰입한경험 == False:
        ss.몰입한경험점수 = 0
        print("몰입한경험 점수업")

    # 점수2
    if ss.마스터피스 == True:
        ss.마스터피스점수 = 10
        print("마스터피스 추가점수업")
    elif ss.마스터피스 == False:
        ss.마스터피스점수 = 0
        print("마스터피스 점수업")

    if ss.마스터피스2 == True:
        ss.마스터피스2점수 = 20
    elif ss.마스터피스2 == False:
        ss.마스터피스2점수 = 0
        print("마스터피스 추가점수업")

    # 점수2
    if ss.증강현실동상 == True:
        ss.증강현실동상점수 = 30
        print("증강현실동상 점수업")
    elif ss.증강현실동상 == False:
        ss.증강현실동상점수 = 0
        print("증강현실동상 점수업")

    # 점수2
    if ss.음악콘서트조명과소리 == True:
        ss.음악콘서트조명과소리점수 = 10
        print("음악콘서트조명과소리 점수업")
    elif ss.음악콘서트조명과소리 == False:
        ss.음악콘서트조명과소리점수 = 0
        print("음악콘서트조명과소리 점수업")

    if ss.음악콘서트조명과소리1 == True:
        ss.음악콘서트조명과소리1점수 == 10
        print("음악콘서트조명과소리1 점수업")
    elif ss.음악콘서트조명과소리1 == False:
        ss.음악콘서트조명과소리1점수 = 0
        print("음악콘서트조명과소리 점수업")

    # 점수2
    if ss.홀로그램연기자 == True:
        ss.홀로그램연기자점수 = 20
        print("홀로그램연기자 점수업")
    elif ss.홀로그램연기자 == False:
        ss.홀로그램연기자점수= 0
        print("홀로그램연기자 점수업")

    if ss.움직이는카메라 == '체크안됨(0점)':
        ss.움직이는카메라점수 = 0
    elif ss.움직이는카메라 == '끝에서3번째(10점)':
        ss.움직이는카메라점수 = 10
    elif ss.움직이는카메라 == '끝에서2번째(20점)':
        ss.움직이는카메라점수 = 20
    elif ss.움직이는카메라 == '끝에서1번째(30점)':
        ss.움직이는카메라점수 = 30
    else:
        ss.움직이는카메라점수 = 0

    # 점수2
    if ss.영화세트장 == True:
        ss.영화세트장점수 = 10
        print("영화세트장 점수업")
    elif ss.영화세트장 == False:
        ss.영화세트장점수 = 0
        print("영화세트장 점수업")

    if ss.영화세트장1 == True:
        ss.영화세트장1점수 = 10
        print("영화세트장 점수업")
    elif ss.영화세트장1 == False:
        ss.영화세트장1점수 = 0
        print("영화세트장 점수업")

    # 점수2
    if ss.사운드믹서 == True:
        ss.사운드믹서점수 = 10
        print("사운드믹서 점수업")
    elif ss.사운드믹서 == False:
        ss.사운드믹서점수 = 0
        print("사운드믹서 점수업")

    # 점수2
    if ss.라이트쇼 == '점수없음(0점)':
        ss.라이트쇼점수 = 0
    elif ss.라이트쇼 == '노란색(10점)':
        ss.라이트쇼점수 = 10
    elif ss.라이트쇼 == '초록색(20점)':
        ss.라이트쇼점수 = 20
    elif ss.라이트쇼 == '파란색(30점)':
        ss.라이트쇼점수 = 30
    else:
        ss.라이트쇼점수 = 0


    # 점수2
    if ss.가상현실아티스트 == True:
        ss.가상현실아티스트점수 = 10
        print("가상현실아티스트 점수업")
    elif ss.가상현실아티스트 == False:
        ss.가상현실아티스트점수 = 0
        print("가상현실아티스트 점수업")

    if ss.가상현실아티스트1 == True:
        ss.가상현실아티스트1점수 = 20
        print("가상현실아티스트 점수업")
    elif ss.가상현실아티스트1 == False:
        ss.가상현실아티스트1점수 = 0
        print("가상현실아티스트 점수업")


    # 점수2
    if ss.공예품창작자 == True:
        ss.공예품창작자점수 = 10
        print("공예품창작자 점수업")
    elif ss.공예품창작자 == False:
        ss.공에품창작자점수 = 0
        print("공에품창작자 점수업")

    if ss.공예품창작자1 == True:
        ss.공예품창작자1점수 = 20
        print("공예품창작자 점수업")
    elif ss.공예품창작자1 == False:
        ss.공에품창작자1점수 = 0
        print("공에품창작자 점수업")
    

    ss.관객이동점수 = (ss.관객이동) * 5
    ss.관객목표이동점수 = (ss.관객목표이동) * 5



    if ss.정밀토큰 == 0:
        ss.정밀토큰점수 = 0
    elif ss.정밀토큰 == 1:
        ss.정밀토큰점수 = 10
    elif ss.정밀토큰 == 2:
        ss.정밀토큰점수 = 15
    elif ss.정밀토큰 == 3:
        ss.정밀토큰점수 = 25
    elif ss.정밀토큰 == 4:
        ss.정밀토큰점수 = 35
    else:
        ss.정밀토큰점수 = 50

    # 점수2
    if ss.샘:
        ss.샘점수 = 10
    else:
        ss.샘점수 = 0

    if ss.안나:
        ss.안나점수 = 10
    else:
        ss.안나점수 = 0

    if ss.노아:
        ss.노아점수 = 10
    else:
        ss.노아점수 = 0

    if ss.이지:
        ss.이지점수 = 10
    else:
        ss.이지점수 = 0

    if ss.에밀리:
        ss.에밀리점수 = 10
    else:
        ss.에밀리점수 = 0


    # 총점 계산 
    ss.score = ss.장비점검점수 + \
               ss.삼디영화관점수 + \
               ss.극장장면전환점수 + \
               ss.몰입한경험점수 + \
               ss.마스터피스점수 + \
               ss.마스터피스2점수 + \
               ss.증강현실동상점수 + \
               ss.음악콘서트조명과소리점수 + \
               ss.음악콘서트조명과소리1점수 + \
               ss.홀로그램연기자점수 + \
               ss.움직이는카메라점수 + \
               ss.영화세트장점수 + \
               ss.영화세트장1점수 + \
               ss.사운드믹서점수 + \
               ss.라이트쇼점수 + \
               ss.가상현실아티스트점수 + \
               ss.가상현실아티스트1점수 + \
               ss.공예품창작자점수 + \
               ss.공예품창작자1점수 + \
               ss.관객이동점수 + \
               ss.관객목표이동점수 + \
               ss.샘점수 + \
               ss.안나점수 + \
               ss.노아점수 + \
               ss.이지점수 + \
               ss.에밀리점수 + \
               ss.정밀토큰점수
    
float_init()

footer_container = st.container()
with footer_container:
    st.write("## score:", ss.score )

footer_container.float("bottom: 0;background-color: rgba(255,255,255,0.8); height: 13vh;text-align:center;padding: 2vh")

st.write('# FLL 2023-2024 점수계산기')

st.checkbox('###### 장비점검(20점)', key='장비점검', on_change=cal_score)
st.write('한쪽출발구역에 모두들어가고 경기점검사시 30.5mm가 넘지않는경우')
st.divider()
st.checkbox('###### 3D영화관(20점) ', key='삼디영화관', on_change=cal_score)
st.write('3D 영화관의 작은 빨간색 빔이 검은색 프레임에 완전히 오른쪽에 위치한경우')
st.divider()
st.write("###### 극장 장면 전환")
st.radio(
    '극장의 빨간색 깃발이 내려가고 현재 장면색상이',
    ('체크안됨(0점)','파란색(10점)', '분홍색(20점)', '주황색(30점)'), key = "극장장면전환", on_change=cal_score)
st.divider()
st.checkbox('###### 몰입한경험(20점) ', key='몰입한경험', on_change=cal_score)
st.write('몰입한 경험 화면 3개가 올라간경우')
st.divider()
st.write("###### 마스터피스")
st.checkbox('마스터피스 예술작품이 조금이라도 박물관목표영역에 걸친경우 10점 ', key='마스터피스', on_change=cal_score)
st.checkbox('마스터피스 예술작품이 받침대위에 완전히 배치된경우 20점추가 ', key='마스터피스2', on_change=cal_score)
st.divider()
st.checkbox('###### 증강현실동상(30점) ', key='증강현실동상', on_change=cal_score)
st.write('증강현실 동상의 주황색 레버가 완전히 오른쪽으로 돌아간경우')
st.divider()
st.write('###### 음악콘서트조명과소리')
st.checkbox('음악콘서트조명과소리(주황색래버가 아래쪽으로 내려간경우 10점) ', key='음악콘서트조명과소리', on_change=cal_score)
st.checkbox('음악콘서트조명과소리(주황색래버가 왼쪽으로 돌아간경우 20점)', key='음악콘서트조명과소리1', on_change=cal_score)
st.divider()
st.checkbox('###### 홀로그램연기자(20점) ', key='홀로그램연기자', on_change=cal_score)
st.write('홀로그램 연기자의 주황색 밀어내기 활성화 장치가 검정색 무대 설정선을 완전히 넘은경우')
st.divider()
st.write('###### 움직이는카메라')
st.radio('움직이는 카메라의 흰색 포인터가 다음의 위치에 있는경우',
         ('점수없음(0점)','끝에서3번째(10점)','끝에서2번째(20점)','끝에서1번째(30점)'), key = "움직이는카메라", on_change=cal_score)
st.divider()
st.write('###### 영화세트장')
st.checkbox('영화세트장(보트가 매트에 닿아있고 검은라인을 완전히 통과한경우 10점) ', key='영화세트장', on_change=cal_score)
st.checkbox('영화세트장(카메라가 매트에 닿아있고 적어도 일부가 카메라 목표영역에 있는경우 10점) ', key='영화세트장1', on_change=cal_score)
st.divider()
st.checkbox('###### 사운드믹서(10점추가) ', key='사운드믹서', on_change=cal_score)
st.write('사운드믹서가 올라간 경우')
st.divider()
st.write("###### 라이트쇼")
st.radio('라이트쇼의 흰색포인터가 다음영역안에 위치한경우 ',
         ('점수없음(0점)','노란색(10점)','초록색(20점)','파란색(30점)'), key='라이트쇼', on_change=cal_score)
st.divider()
st.write('###### 가상현실아티스트')
st.checkbox('가상현실아티스트(닭이 손상되지않고 시작위치에서 움직인경우 10점) ', key='가상현실아티스트', on_change=cal_score)
st.checkbox('가상현실아티스트(보라색점을 넘거나 완전히 지나가면 20점추가) ', key='가상현실아티스트1', on_change=cal_score)
st.divider()
st.write('###### 공예품창작자')
st.checkbox('공예품창작자(공예기계의 주황색 흰색덮개가 완전히 열린경우 10점) ', key='공예품창작자', on_change=cal_score)
st.checkbox('공예품창작자(공예기계의 연분홍색 걸쇠가 완전히 아래로 향한경우 20점) ', key='공예품창작자1', on_change=cal_score)
st.divider()
st.slider('###### 관객이동',min_value=0,max_value=7,value=0, key='관객이동', on_change=cal_score)
st.slider('###### 관객목표이동',min_value=0,max_value=7,value=0, key='관객목표이동', on_change=cal_score)
st.write("각 5점")
st.divider()
st.write('###### 전문가 이동')
st.write("각 10점")
st.toggle('###### 무대매니저 샘', key='샘',on_change=cal_score)
st.toggle('###### 큐레이터 안나', key='안나',on_change=cal_score)
st.toggle('###### 사운드엔지니어 노아', key='노아',on_change=cal_score)
st.toggle('###### 스케이트파크 이지', key='이지',on_change=cal_score)
st.toggle('###### 시각효과감독 에밀리', key='에밀리',on_change=cal_score)
st.slider('###### 정밀토큰 ',min_value=0,max_value=6,value=0, key='정밀토큰', on_change=cal_score)
st.write("#### -끝(만점550점)-")