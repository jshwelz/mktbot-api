import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Input, InputRightElement, InputGroup, Button, SimpleGrid } from '@chakra-ui/react'



function Home() {
    const navigateTo = useNavigate();
    const [username, setUserName] = useState('');
    const handleClick = () => {
        navigateTo('/chat', { state: { username } });
    };
    const handleChange = (event: any) => {
        setUserName(event.target.value);
    };

    return (
        <SimpleGrid columns={2} spacingX='40px' spacingY='20px'>
            <InputGroup size='md'>
                <Input
                    pr='4.5rem'
                    type='text'
                    placeholder='Enter Your Name'
                    value={username}
                    onChange={handleChange}
                />
                <InputRightElement width='4.5rem'>
                    <Button h='1.75rem' size='sm' onClick={handleClick}>
                        Enter
                    </Button>
                </InputRightElement>
            </InputGroup>
        </SimpleGrid>
    )
}

export default Home;
