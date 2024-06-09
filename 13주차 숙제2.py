#김우준 2024133519

#1번

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 검색어와 검색 URL을 설정합니다.
search_keywords = ['원피스', '블리치', '나루토', '주술회전', '스파이패밀리']

# 검색 결과를 저장할 리스트를 초기화합니다.
book_info = []

# 각 검색어에 대해 책 정보를 가져옵니다.
for keyword in search_keywords:
    # 네이버 검색 URL을 설정합니다.
    url = f'https://search.naver.com/search.naver?query={keyword} 책'
    
    # 페이지를 요청하고 응답을 받습니다.
    response = requests.get(url)
    
    # 응답이 성공적으로 도착했는지 확인합니다.
    if response.status_code == 200:
        # BeautifulSoup 객체를 생성합니다.
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 책 제목과 저자를 추출합니다.
        titles = soup.find_all('a', class_='api_txt_lines total_tit')
        authors = soup.find_all('span', class_='txt_block')
        
        # 책 정보를 리스트에 추가합니다.
        for title, author in zip(titles, authors):
            book_info.append({
                '책 제목': title.get_text(),
                '저자': author.get_text(),
                '출판사': '네이버',
                '장르': keyword  # 새로운 정보인 '장르'를 추가합니다.
            })

# 데이터프레임을 생성합니다.
df = pd.DataFrame(book_info)

# 결과를 출력합니다.
print(df)

#2번

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_cnt(isbn):
    # 네이버 책 검색 API를 활용하여 책의 상세 정보를 가져옵니다.
    url = f'https://openapi.naver.com/v1/search/book_adv.xml?d_isbn={isbn}'
    headers = {'X-Naver-Client-Id': 'YOUR_CLIENT_ID', 'X-Naver-Client-Secret': 'YOUR_CLIENT_SECRET'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'xml')
    
    # 책의 쪽수 정보를 추출합니다.
    page_cnt = soup.find('page').get_text()
    
    return page_cnt

# 검색어와 ISBN을 포함하는 딕셔너리를 생성합니다.
search_books = {'원피스': '9788925286587', '블리치': '9788934971410', '나루토': '9784062565013', '주술회전': '9788970129047', '스파이패밀리': '9788950973347'}

# 검색 결과를 저장할 리스트를 초기화합니다.
book_info = []

# 각 검색어에 대해 책 정보를 가져옵니다.
for keyword, isbn in search_books.items():
    # 네이버 검색 URL을 설정합니다.
    url = f'https://search.naver.com/search.naver?query={keyword} 책'
    
    # 페이지를 요청하고 응답을 받습니다.
    response = requests.get(url)
    
    # 응답이 성공적으로 도착했는지 확인합니다.
    if response.status_code == 200:
        # BeautifulSoup 객체를 생성합니다.
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 책 제목과 저자를 추출합니다.
        titles = soup.find_all('a', class_='api_txt_lines total_tit')
        authors = soup.find_all('span', class_='txt_block')
        
        # 책 정보를 리스트에 추가합니다.
        for title, author in zip(titles, authors):
            page_cnt = get_page_cnt(isbn)  # 책의 쪽수를 가져옵니다.
            book_info.append({
                '책 제목': title.get_text(),
                '저자': author.get_text(),
                '출판사': '네이버',
                '장르': keyword,
                '쪽수': page_cnt  # 책의 쪽수 정보를 추가합니다.
            })

# 데이터프레임을 생성합니다.
df = pd.DataFrame(book_info)

# 결과를 출력합니다.
print(df)
