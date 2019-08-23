#include "Fixture.h"

#ifdef __cplusplus // Need to extern to C compiler
extern "C" {
#endif

#include "FakeServices.h"

using namespace EmbeddedCUnitTest;

namespace EmbeddedC 
{
	std::unique_ptr<MathsService> _math;
  
  // Defining actual function call to return reference to our mock
  int multiply(int p1, int p2)
	{
		return TestFixture::_math->multiply(p1, p2);
	}
  
}

#ifdef __cplusplus
}
#endif
