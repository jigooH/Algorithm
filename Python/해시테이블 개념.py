'''
해시 테이블은 key와 value를 맵핑한 자료 구조
딕셔너리나 collections.defualtdict 을 활용하면 됨
'''

age_mapper = {}
age_mapper['철수'] = 20     # 신규 값 추가
age_mapper['철수'] += 1     # 기존 값 갱신
print(age_mapper['철수'])   # 21

del age_mapper['철수']      # '철수'에 해당하는 매핑을 삭제
                            # 이거 잘 사용할 경우는 없을텐데 매핑값 지워야 할때 사용