import axios from 'axios'

const getDetails = async (id) => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/get_detailed_stats'
  const response = await axios.get(`${url}?id=${id}`)
  return response.data
}

export default getDetails;