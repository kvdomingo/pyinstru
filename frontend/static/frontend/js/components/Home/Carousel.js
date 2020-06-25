import React from 'react';
import {
    MDBCarousel as Carousel,
    MDBCarouselInner as CarouselInner,
    MDBCarouselItem as CarouselItem,
    MDBCarouselCaption as CarouselCaption,
    MDBView as View,
    MDBContainer as Container,
    MDBMask as Mask,
} from 'mdbreact';
import { Image } from 'cloudinary-react';


export default function IntroCarousel() {
    const ar = (window.screen.width/window.screen.height).toFixed(2);
    return (
        <Container fluid className='px-0'>
            <Carousel
                className='main-carousel py-0 my-0'
                activeItem={1}
                length={3}
                showControls
                showIndicators
                >
                <CarouselInner>

                    <CarouselItem itemId='1'>
                        <View>
                            <Image
                                cloudName='kdphotography-assets'
                                className='img-fluid'
                                publicId='ipl/ipl_grp'
                                secure
                                responsive
                                responsiveUseBreakpoints
                                width='auto'
                                dpr='auto'
                                crop='fill'
                                aspectRatio={ar}
                                />
                            <Mask overlay='black-light' />
                        </View>
                        <CarouselCaption>
                            <p className='lead'>
                                Mentoring the next generation of physicists and applied physicists for Philippine Society
                            </p>
                            <p>
                                The Instrumentation Physics Laboratory (IPL) is one of the research laboratories in the National Institute of Physics, College of Science, University of the Philippines Diliman. IPL currently has 5 full-time Ph.D. faculty supervising 54 student-members (7 Ph.D., 11 M.S., 36 BS) under 5 research subgroups.
                            </p>
                        </CarouselCaption>
                    </CarouselItem>

                    <CarouselItem itemId='2'>
                        <View>
                            <Image
                                cloudName='kdphotography-assets'
                                className='img-fluid'
                                publicId='ipl/csdean'
                                secure
                                responsive
                                responsiveUseBreakpoints
                                width='auto'
                                dpr='auto'
                                crop='fill'
                                gravity='north'
                                aspectRatio={ar}
                                />
                            <Mask overlay='black-light' />
                        </View>
                        <CarouselCaption>
                            <p>Congratulations to Dr. Giovanni A. Tapang for his appointment as the 7th Dean of the College of Science. His deanship was formally affirmed by UP Diliman Chancellor Dr. Michael L. Tan last 8 October 2019.</p>
                        </CarouselCaption>
                    </CarouselItem>

                    <CarouselItem itemId='3'>
                        <View>
                            <Image
                                cloudName='kdphotography-assets'
                                className='img-fluid'
                                publicId='ipl/welcome19'
                                secure
                                responsive
                                responsiveUseBreakpoints
                                width='auto'
                                dpr='auto'
                                crop='fill'
                                gravity='north'
                                aspectRatio={ar}
                                />
                            <Mask overlay='black-light' />
                        </View>
                        <CarouselCaption>
                            <p>Last October 14, 2019 (Monday), IPL welcomed its two new members, Bea Movido and Karl Aleta. Bea and Karl have successfully completed the month-long IPL Application Process which took place in September. Bea's and Karl's undergraduate researches are being supervised by Dr. Caesar Saloma and Dr. Johnrob Bantang, respectively.</p>
                        </CarouselCaption>
                    </CarouselItem>

                </CarouselInner>
            </Carousel>
        </Container>
    );
}