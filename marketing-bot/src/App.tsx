import { useState } from 'react'
import { ChakraProvider } from '@chakra-ui/react'
import { ReactNode } from 'react';
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink, Grid, GridItem
} from '@chakra-ui/react'

import {
  Box,
  Flex,
  Avatar,
  HStack,
  Link,
  IconButton,
  Button,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  MenuDivider,
  useDisclosure,
  useColorModeValue,
  Stack,
} from '@chakra-ui/react';
import { ChevronRightIcon } from '@chakra-ui/icons'
import { HamburgerIcon, CloseIcon } from '@chakra-ui/icons';


import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/home';
import Chatbot from './components/chatbot';
import DashBoard from './components/dashboard';


const Links = [{ 'title': 'Home', 'link': '' }, { 'title': 'Chat', 'link': 'chat' }, { 'title': 'Statistics', 'link': 'dashboard' }];

const NavLink = ({ children }: { children: ReactNode }) => (
  <Link
    px={2}
    py={1}
    rounded={'md'}
    _hover={{
      textDecoration: 'none',
      bg: useColorModeValue('gray.200', 'gray.700'),
    }}
    href={''}>
    {children}
  </Link>
);


function App() {

  const { isOpen, onOpen, onClose } = useDisclosure();
  return (

    <>

      <Box bg={useColorModeValue('gray.100', 'gray.900')} px={4}>
        <Flex h={16} alignItems={'center'} justifyContent={'space-between'}>
          <IconButton
            size={'md'}
            icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
            aria-label={'Open Menu'}
            display={{ md: 'none' }}
            onClick={isOpen ? onClose : onOpen}
          />
          <HStack spacing={8} alignItems={'center'}>
            {/* <Box>Logo</Box> */}
            <HStack
              as={'nav'}
              spacing={4}
              display={{ base: 'none', md: 'flex' }}>
              <Link
                px={2}
                py={1}
                rounded={'md'}
                _hover={{
                  textDecoration: 'none',
                  bg: useColorModeValue('gray.200', 'gray.700'),
                }}
                href='/'>
                Home
              </Link>
              <Link
                px={2}
                py={1}
                rounded={'md'}
                _hover={{
                  textDecoration: 'none',
                  bg: useColorModeValue('gray.200', 'gray.700'),
                }}
                href='/chat'>
                Chat
              </Link>
              <Link
                px={2}
                py={1}
                rounded={'md'}
                _hover={{
                  textDecoration: 'none',
                  bg: useColorModeValue('gray.200', 'gray.700'),
                }}
                href='/dashboard'>
                Statistics
              </Link>

            </HStack>
          </HStack>

        </Flex>


      </Box>

      <Box p={4}>
        <Router>
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/chat' element={<Chatbot />} />
            <Route path='/dashboard' element={<DashBoard />} />
          </Routes>
        </Router>


      </Box>

    </>
  )
}

export default App
