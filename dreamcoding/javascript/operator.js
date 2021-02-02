function solution(next_student) {
    // 학생 0번째 인덱스에 0 삽입 1번째부터 맞추기 위해
    next_student.splice(0, 0, 0)
    console.log('배열', next_student)
    let ansObj = {}
    let len = next_student.length
    for (let i = 1; i < len; i ++) {
        let cnt = 1
        if (next_student[i] == 0) {
            ansObj[i] = 1
        } else {
            let target = next_student[i]
            console.log(target)
            while (target > 1 && target != i) {
                target = next_student[target]
                cnt += 1
            }
            ansObj[i] = cnt
        }
    }
    console.log(ansObj)
    console.log('hello')
    var answer = 0;
    return answer;
}
solution ();