import axios from 'axios'

const getInitatives = async () => {
  const url = 'https://us-central1-seoranking-324303.cloudfunctions.net/get_initiatives'
  const response = await axios.get(`${url}`)
  return response.data.items
}

export default getInitatives;