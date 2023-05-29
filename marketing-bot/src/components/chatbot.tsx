import React from 'react';
import { useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';
import {
    Card, CardHeader, CardBody, Heading, Stack, Box, Text, StackDivider, Button,
    SimpleGrid, Image
} from '@chakra-ui/react'
import ticketsImage from "../assets/goodbye.avif"

function Chatbot() {
    const location = useLocation();
    const username = location.state?.username;
    const [data, setData] = useState({ data: {} });
    const [loadData, setLoadData] = useState({ data: {} });
    const [user_id, setUserID] = useState('');
    const [showResults, setShowResults] = React.useState(false)
    const [showResultsNo, setShowResultsNo] = React.useState(false)


    const postData = async (query = "Hello") => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id, username, query_input: query })
        };
        try {
            const response = await fetch('http://127.0.0.1:8000/api/v1/chatbot/', requestOptions);
            if (!response.ok) {
                throw new Error(`Error! status: ${response.status}`);
            }
            const result = await response.json();
            console.log('result is: ', JSON.stringify(result, null, 4));
            setUserID(result.data.user_id)

            if (result.data.name == "greeting") {
                setShowResults(false)
                setLoadData(result)

            } else if (result.data.name == "turndown") {
                setShowResultsNo(true)
                setShowResults(false)
                setData(result)
            } else {
                setShowResults(true)
                setShowResultsNo(false)
                setData(result)
            }
        } catch (err) {

        } finally {

        }

    };

    const redeemCoupon = async (query = "Redeem") => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id, username, query_input: query })
        };
        try {
            const response = await fetch('http://127.0.0.1:8000/api/v1/redeem/', requestOptions);
            if (!response.ok) {
                throw new Error(`Error! status: ${response.status}`);
            }
            const result = await response.json();
            console.log('result is: ', JSON.stringify(result, null, 4));
        } catch (err) {

        } finally {

        }

    };

    useEffect(() => {
        postData();
    }, []);

    const ResultCoupon = () => (
        <Box>
            <Card>
                <CardHeader>
                    <Heading size='md'>Coupon Template</Heading>
                </CardHeader>
                <CardBody>
                    <Stack divider={<StackDivider />} spacing='4'>
                        <Box>
                            <Text pt='2' fontSize='sm'>
                                {data.data.response}
                            </Text>
                        </Box>
                        <Box>
                            <Button colorScheme='blue' onClick={() => redeemCoupon("Reveal")} variant='outline'>
                                Reveal Coupon
                            </Button>
                        </Box>
                    </Stack>
                </CardBody>
            </Card>
        </Box>
    )
    const ResultNo = () => (
        <Box>
            <Card>
                <CardHeader>
                    <Heading size='md'>Media Template</Heading>
                </CardHeader>
                <CardBody>
                    <Stack divider={<StackDivider />} spacing='4'>
                        <Box boxSize='sm'>
                            <Image src={ticketsImage} />
                        </Box>
                        <Box>
                            <Text pt='2' fontSize='sm'>
                                {data.data.response}
                            </Text>
                        </Box>
                    </Stack>
                </CardBody>
            </Card>
        </Box>
    )


    return (
        <SimpleGrid columns={2} spacingX='40px' spacingY='20px'>
            <Box>
                <Card>
                    <CardHeader>
                        <Heading size='md'>Marketing Bot</Heading>
                    </CardHeader>

                    <CardBody>
                        <Stack divider={<StackDivider />} spacing='4'>
                            <Box>
                                <Text pt='2' fontSize='sm'>
                                    Hello {username}
                                </Text>
                                <Text pt='2' fontSize='sm'>
                                    {loadData.data.response}
                                </Text>
                            </Box>
                            <Button colorScheme='blue' onClick={() => postData("Yes")} variant='outline'>
                                Yes! Show me the Cuppon
                            </Button>
                            <Box>
                                <Button colorScheme='blue' onClick={() => postData("No")} variant='outline'>
                                    No! thanks
                                </Button>
                            </Box>
                        </Stack>
                    </CardBody>
                </Card>
            </Box>
            {showResults ? <ResultCoupon /> : null}
            {showResultsNo ? <ResultNo /> : null}
        </SimpleGrid>
    );
}

export default Chatbot;
