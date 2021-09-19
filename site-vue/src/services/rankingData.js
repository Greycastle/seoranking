
const mockData = {
  rankings: [
    {
      site: 'greycastle.se',
      keyword: 'greycastle flutter',
      lastRanking: 1,
      lastConfirmed: new Date(),
      rankingsTotal: 12
    }
  ],
  account: {
    ranksTotal: 23,
    ranksRemaining: 7,
    rankSchedule: 3
  }
}

const getRankingData = () => {
  return new Promise((resolve) => {
    setTimeout(() => { resolve(mockData) }, 13500)
  })
}

export default getRankingData;