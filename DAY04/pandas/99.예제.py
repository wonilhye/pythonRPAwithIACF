import csv

file = open("파일 경로")
csv = csv.reader(file)

for i in csv:
    if i[2] == 'SALESMAN':
        print(i[1], i[2])

for i in csv:
    if int(i[5]) >= 3000:
        print(i[1], i[5], i[2])

for i in csv:
    if i[2] == 'SALESMAN' and int(i[5]) >= 1000:
        print(i[1], i[5], i[2])

csv[['ename','sal']]     #emp에서 ename, sal 컬럼을 출력

#emp에서 ename, sal 컬럼을 출력하는데
#직업이 SALESMAN인 것만 출력
csv[['ename', 'job']][csv['job'] == 'SALESMAN']

#직업이 SALESMAN이고 월급이 1000이상인 사람들의 이름, 월급, 직업을 출력한다.
csv[['ename', 'sal', 'job']] [(csv['job'] == 'SALESMAN') & (csv['sal'] >= 1000)]

#부서번호가 10번, 20번인 사원들의 이름과 부서번호를 출력
csv[['ename', 'deptno']][csv['deptno'].isin([10,20])]

#월급이 1000에서 3000사이 사원들의 이름과 월급을 출력
csv[['ename','sal']][csv['sal'].between(1000, 3000)]

#직업이 SALESMAN, ALALYST가 아닌 사원들의 이름과 직업
csv[['ename','job']][~ csv['job'].isin(['SALESMAN', 'ALALYST'])]

#직업이 NULL값이 아닌 아닌 사원들의 이름과 직업
csv[['ename','job']][~ csv['job'].isnull()]