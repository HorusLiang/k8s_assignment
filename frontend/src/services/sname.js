import axios from 'axios'
const baseUrl = process.env.REACT_APP_BASE_URL || 'http://localhost:5001/'

const getAll=async ()=>{
    const request=axios.get(baseUrl)
    return request.then(response=>response.data)
}
const createNew=async (fullname)=>{
    const request = axios.post(baseUrl, fullname)
    return request.then(response => response.data)
}

export default { getAll,createNew}
