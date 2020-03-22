import axios from 'axios'

const proxy='https://www.fastmock.site/mock/c44d08ff131933059ee720ac232910e4/test'

export function fetchWordCloud() {
    const url =proxy+'/paper/findMsgByWordCloud'
    return axios.get(url)
}