# 51 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다.
#    영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 52 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("배트맨")
print(movie_rank)

# 53 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
#    "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 54 movie_rank 리스트에서 '럭키'를 삭제하라.
del movie_rank[3]
print(movie_rank)

# 55 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
del movie_rank[3]
movie_rank.pop()
print(movie_rank)

# 56 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 57 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))

# 58 다음 리스트의 합을 출력하라.
nums2 = [1, 2, 3, 4, 5]
print(sum(nums2))

# 59 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60 다음 리스트의 평균을 출력하라.
nums3 = [1, 2, 3, 4, 5]
print(sum(nums3)/len(nums3))
