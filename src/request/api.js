import axios from 'axios'

const proxy='https://www.fastmock.site/mock/c44d08ff131933059ee720ac232910e4/test'
//const proxy='.'

export function fetchWordCloud() {
    const url =proxy+'/paper/findMsgByWordCloud'
    return axios.get(url)
}

export function fetchBarChart(value) {
    const url =proxy+'/paper/findFigure1ByWC?wordCloud='+value
    return axios.get(url)
}

export function fetchCloudChart(value) {
    const url =proxy+'/paper/findFigure2ByWC?wordCloud='+value
    return axios.get(url)
}

export function fetchPieChart(value) {
    const url =proxy+'/paper/findFigure3ByWC?wordCloud='+value+'&year=All'
    return axios.get(url)
}

export function fetchPaper(value) {
    const url =proxy+'/paper/findFigure1Meet?wordCloud='+value+'&year=All'
    return axios.get(url)
}