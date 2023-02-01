import axios from 'axios'
const baseUrl = 'http://127.0.0.1:5001/'

const getAll=async ()=>{
    const request=axios.get(baseUrl)
    return request.then(response=>response.data)
}
const createNew=async (fullname)=>{
    const request = axios.post(baseUrl, fullname)
    return request.then(response => response.data)
}

export default { getAll,createNew}
