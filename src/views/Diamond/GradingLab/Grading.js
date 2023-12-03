import React from "react";
import StyledContainer from "../components/StyledContainer";
import { useState, useEffect } from "react";
import {
  Image,
  useToast,
  Table,
  Button,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
} from "@chakra-ui/react";

// assets
import gradingbg from '../../../assets/img/process/crave.png';
import diamondImage from "assets/img/DiamondType/cut.png";

export default function GradingLab() {
  const [diamonds, setDiamonds] = useState([]);
  const toast = useToast();

  //get cut diamond from server 
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/carve/view`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(),
    })
      .then(response => response.json()) // parse JSON from request
      .then(data => {
        // parse data because data is in JSON format
        const parsedData = JSON.parse(data);
        if (Array.isArray(parsedData)) {
          setDiamonds(parsedData);
        } else {
          setDiamonds([
          ]);
        }
      })
      .then(() => {
        if (diamonds.length === 0) {
          toast({
            title: "No Diamond",
            description: "There is no diamond to be carved.",
            status: "info",
            duration: 5000,
            isClosable: true,
          });
        }
      })
      .catch((error) => {
        console.error("Failed to show your mined diamond :", error);
        toast({
          title: "Show Failed",
          description: "Unable to connect to the server.",
          status: "error",
          duration: 5000,
          isClosable: true,
        });
      });
  }, []); // empty dependency array means this effect will only run once 

  // !!!need to change url
  // carve diamond
  const handleCutClick = async (diamond) => {
    const response = fetch(`http://127.0.0.1:8000/process/processDiamonds/${diamondID}/${companyNum}/${address}`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        diamondID: diamond.diamondID,
        companyNum: diamond.companyNum,
        address: diamond.address
      }),
    })
    if (response.ok) {
      toast({
        title: "Cutting Successful",
        description: "The diamond status has been updated to cut.",
        status: "success",
        duration: 5000,
        isClosable: true,
      });
    }
    else {
      toast({
        title: "Cutting Failed",
        description: "Unable to connect to the server.",
        status: "error",
        duration: 5000,
        isClosable: true,
      });
    }
  };

  return (
    <StyledContainer backgroundImage={gradingbg} pt="10%">
      <Table variant="simple" >
        <Thead>
          <Tr>
            <Th>cut Diamond</Th>
            <Th>Unique ID</Th>
            <Th>Company Number</Th>
            <Th>Action</Th>
          </Tr>
        </Thead>
        <Tbody>
          {diamonds.map((diamond) => (
            <Tr key={diamond.UniqueId}>
              <Td style={{ textAlign: 'center' }}>
                <Image src={diamondImage} boxSize="50px" objectFit="cover" />
              </Td>
              <Td style={{ textAlign: 'center' }}>{diamond.ProductId}</Td>
              <Td style={{ textAlign: 'center' }}>{diamond.UniqueId}</Td>
              <Td >
                <Button
                  colorScheme="teal"
                  size="sm"
                  onClick={() => handleCarvedClick(diamond)}
                >
                  Carve it
                </Button>
              </Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </StyledContainer>

  );
}
