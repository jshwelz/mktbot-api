import { useEffect, useState } from 'react';
import {
  Stat,
  StatLabel,
  StatNumber,
  StatGroup,
} from '@chakra-ui/react'


function DashBoard() {
  const [stats, setStats] = useState({})

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/stats/").then((response) =>
      response.json()
    ).then((data) => {
      console.log(data)
      setStats({ "coupons": data.data['coupons_redeem'], "turndown": data.data['turndown'] })
    }
    )
  }, [])

  return (

    <StatGroup>
      <Stat>
        <StatLabel>Coupons Redeem</StatLabel>
        <StatNumber>{stats.coupons}</StatNumber>
      </Stat>
      <Stat>
        <StatLabel>Coupons Rejections</StatLabel>
        <StatNumber>{stats.turndown}</StatNumber>
      </Stat>
    </StatGroup>

  );
}

export default DashBoard;
