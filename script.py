import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.naver.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["purple", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "김동찬")
write("description", "소개서")
write("button", "인스타주소")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "현재 재학중인 학교": "지산중학교",
  "생년월일": "2007/03/16",
  "나이": "16",
  "전화번호": "010-3663-4653"
}
information(informations)
