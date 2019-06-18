from bs4 import BeautifulSoup

html = '''
<td class="title">
	<div class="tit3">
		<a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
	</div>
</td>'''

# 1. tag 조회
def beautifulSoup(html, par):
    return html


def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)
    # print(type(bs))

    tag = bs.a
    # print(tag)
    # print(type(tag))

    tag = bs.td.div
    print(tag)
    print(type(tag))



# 2. attribute 값 가져오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])

    tag = bs.div
    print(tag['id'])


if __name__ == '__main__':
    ex1()
    ex2()